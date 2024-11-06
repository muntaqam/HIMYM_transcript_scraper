import requests
from bs4 import BeautifulSoup
import csv
import re

# URL of the main page with all episodes
main_page_url = "https://transcripts.foreverdreaming.org/viewforum.php?f=177"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}

# Function to scrape episodes for a given season
def scrape_season(season_code, csv_filename):
    # Open CSV file to write data
    with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["episode", "name", "line"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Step 1: Get the main page content
        response = requests.get(main_page_url, headers=headers)
        main_soup = BeautifulSoup(response.text, "html.parser")

        # Step 2: Find all episode links for the specified season
        episode_links = []
        for episode in main_soup.find_all("a", class_="topictitle"):
            episode_title = episode.get_text(strip=True)

            # Extract only the episode code for the specified season (e.g., "07x")
            episode_code_match = re.match(f"({season_code}x\\d+)", episode_title)
            if episode_code_match:
                episode_code = episode_code_match.group(1)
                episode_links.append((episode_code, episode['href']))

        # Sort episode links by episode code in ascending order
        episode_links.sort(key=lambda x: int(x[0].split("x")[1]))

        # Step 3: Visit each episode page and scrape the transcript
        for episode_code, episode_link in episode_links:
            episode_url = "https://transcripts.foreverdreaming.org" + episode_link[1:]  # Remove initial './' from URL
            response = requests.get(episode_url, headers=headers)
            episode_soup = BeautifulSoup(response.text, "html.parser")

            # Find the main container for the transcript
            transcript_container = episode_soup.find("div", class_="content")

            # Check if the container was found
            if transcript_container:
                # Step 4: Process each line in the transcript
                for line in transcript_container.stripped_strings:
                    # Split line by the first colon to separate character and dialogue
                    parts = line.split(":", 1)
                    if len(parts) == 2:
                        character = parts[0].strip()
                        dialogue = parts[1].strip()
                    else:
                        character = "Unknown"  # Default to "Unknown" if no colon is found
                        dialogue = parts[0].strip()

                    # Only add to CSV if dialogue is present
                    if dialogue:
                        writer.writerow({
                            "episode": episode_code,  # Only the code, like "07x24"
                            "name": character,
                            "line": dialogue
                        })

                print(f"Scraped {episode_code}")
            else:
                print(f"Transcript container not found for {episode_code}")

# Run the scraper for Seasons 7, 8, and 9, each saving to a different CSV file
scrape_season("07", "himym_season7.csv")
scrape_season("08", "himym_season8.csv")
scrape_season("09", "himym_season9.csv")
