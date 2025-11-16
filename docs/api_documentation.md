📘 API Documentation

This document describes the key modules, classes, and functions used in the AI Capstone project.

## 1. Module: src/scraper/nitter_scraper.py
### Class: NitterScraper
Methods:
__init__(self, driver, username)

Initializes the scraper.

Parameter	Description
driver	Selenium WebDriver instance
username	Twitter/X username to scrape
scroll_and_collect(self)

Scrolls through the profile page and extracts tweet containers.

Returns:
List of Selenium elements representing tweets.

parse_tweet(self, tweet_element)

Extracts structured data from a single tweet.

Returns a dictionary with keys:
tweet_id
timestamp
text
comments
retweets
likes
urls
is_retweet
scrape(self)

Main method: collects and parses all tweets from the user.

Returns:
List of tweet dictionaries.

## 2. Module: src/scraper/data_collector.py
### Function: load_raw_data(file_path)

Loads a CSV containing raw tweets.

Parameter	Description
file_path	Path to raw tweet file

Returns: Pandas DataFrame.

Function: clean_text(text)

Cleans tweet text by:

Removing URLs

Removing emojis

Removing punctuation

Removing stopwords

Converting to lowercase

Returns: cleaned text string.

Function: process_raw_data(raw_df)

Applies preprocessing steps to the entire dataset.

Returns: cleaned dataframe.

Function: save_processed_data(df, output_path)

Saves cleaned dataset to data/processed/.

## 3. Module: src/selenium_scraper.py
Function: get_driver()

Creates a Selenium WebDriver instance with configuration.

Function: scrape_user(username)

Runs the scraper for a given username and saves output to:

data/raw/{username}_tweets.csv

Main Script Execution

When running:

python src/selenium_scraper.py


The script:

Opens browser

Loads Nitter profile

Scrapes tweets

Saves CSV file

## Notes

URLs are extracted directly from anchor tags.

Engagement metrics are parsed from tweet HTML.

Retweet detection is based on markers like “REPOST” or “RETWEET”.