# python-bs4-web-scraping

## Overview

This project involves web scraping multiple websites using BeautifulSoup (bs4) to extract the most common words and their frequencies. The collected data is then processed, translated using Deepl, and analyzed to find common words among different websites. The results are presented in various CSV files, providing insights into word frequency and commonalities across different web pages.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/KeremDUZENLI/python-bs4-web-scraping.git
   ```

2. Navigate to the project directory:

   ```bash
   cd python-bs4-web-scraping
   ```

3. Install the required dependencies:

   ```bash
   pip install requests
   pip install beautifulsoup4
   pip install nltk
   python -m nltk.downloader all
   pip install --upgrade deepl
   ```

4. Set up your environment variables:

   Create a `.env` file with the following content:

   ```
   DEEPL_KEY=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx:xx
   ```

   Replace `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx:xx` with your Deepl API key.

## Usage

1. Run the main script to scrape websites, process data, and generate CSV files:

   ```bash
   python main.py
   ```

   This will execute the entire pipeline, including web scraping, translation, and common word analysis.

2. Explore the generated CSV files in the `csv` directory for detailed information on word frequency and commonalities.

## Project Structure

- `main.py`: Main script to execute the entire pipeline.
- `tool/`: Directory containing utility functions for directory setup and environment variable retrieval.
- `web/`: Directory containing web scraping and translation functions.
- `csv/`: Directory to store the generated CSV files.
- `README.md`: Project documentation.

## Dependencies

- `requests`: For making HTTP requests.
- `bs4` (Beautiful Soup): For parsing HTML content.
- `nltk` (Natural Language Toolkit): For natural language processing tasks.
- `deepl`: For translating text using Deepl API.
