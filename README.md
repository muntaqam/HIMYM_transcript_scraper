HIMYM Episode Transcript Scraper
This repository contains a Python script to scrape episode transcripts from a fan-made "How I Met Your Mother" forum. The script retrieves transcript data for selected seasons, processes the dialogue to identify speakers, and saves the output to CSV files for further analysis or study.

Features
Scrapes Transcripts for Specific Seasons: Collects all dialogue lines for seasons 7, 8, and 9 (or any specified season) from the forum.
Speaker Identification: Attempts to identify the character speaking each line. If the speaker is unknown, the script tags it as "Unknown."
Structured CSV Output: Saves each season’s transcripts to a separate CSV file with columns for episode, speaker name, and dialogue.
Requirements
Python 3.x
BeautifulSoup4 and Requests libraries (for web scraping)
Install them using:
bash
Copy code
pip install beautifulsoup4 requests
Usage
1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/himym-transcript-scraper.git
cd himym-transcript-scraper
2. Run the Script
To scrape transcripts for a specific season, use:

bash
Copy code
python scrape_himym.py
This will generate three CSV files:

himym_season7.csv
himym_season8.csv
himym_season9.csv
Each file contains the following columns:

episode – Episode code (e.g., 07x24)
name – Character name (or "Unknown" if not identified)
line – Dialogue spoken by the character
Customization
Season Selection: You can modify the scrape_season function call in the script to scrape additional seasons by changing the season code and CSV filename.
Episode Filtering: The script is currently set to scrape only episodes with codes starting with specific season numbers. You can change this behavior by modifying the season_code parameter.
Script Details
The script operates in the following steps:

Fetch Episode List: Accesses the main page with all episode links for the chosen season.
Filter Episodes by Season Code: Filters episodes to match only the specified season codes.
Scrape Individual Episode Transcripts: Navigates to each episode page, identifies speaker names and dialogue lines, and handles cases where the speaker name is missing by marking it as "Unknown."
Save to CSV: Saves each line of dialogue, along with its speaker and episode code, to a structured CSV file.
Example Output
Each CSV file will look like:

episode	name	line
07x01	Ted	"Kids, if there's one big theme to this story..."
07x01	Unknown	"(chuckling)"
07x01	Barney	"What do you think of this tie?"
Troubleshooting
Missing Characters: Some lines might not have character names. In these cases, the script tags the speaker as "Unknown."
Connection Issues: If the script fails to retrieve pages, ensure you have a stable internet connection and check the site’s availability.
Forum Layout Changes: The script relies on specific HTML tags and classes. If the website layout changes, the script may need adjustments to continue working correctly.
Contributing
Contributions are welcome! If you encounter issues or have ideas for improvements, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License.
