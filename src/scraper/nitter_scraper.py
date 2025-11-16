import requests
from bs4 import BeautifulSoup
import time
import random
import yaml


class NitterScraper:
    def __init__(self, config_path="config/config.yaml"):
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)

        self.base_urls = config["nitter_instances"]
        self.delay = config["scraper"]["delay"]
        self.headers = {"User-Agent": config["scraper"]["user_agent"]}

    def fetch_page(self, url):
        """Fetch HTML content from Nitter with delay and error handling."""
        time.sleep(self.delay + random.uniform(0, 1))

        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"Request failed: {e}")
            return None

    def parse_tweets(self, html):
        """Extract tweets from the page."""
        soup = BeautifulSoup(html, "html.parser")
        tweets = soup.find_all("div", class_="timeline-item")

        parsed_data = []
        for tweet in tweets:
            content = tweet.find("div", class_="tweet-content")
            timestamp = tweet.find("span", class_="tweet-date")
            stats = tweet.find_all("span", class_="tweet-stat")

            parsed_data.append({
                "text": content.text.strip() if content else "",
                "timestamp": timestamp.text.strip() if timestamp else "",
                "stats": [s.text.strip() for s in stats] if stats else [],
            })

        return parsed_data

    def scrape_user(self, username):
        """Scrape multiple pages of tweets for a given user with retry logic."""
        all_tweets = []
        page = 1
        retries = 0
        max_retries = 3

        while retries < max_retries:
            try:
                base_url = random.choice(self.base_urls)
                url = f"{base_url}/{username}?page={page}"
                print(f"Scraping {url}")

                html = self.fetch_page(url)
                if not html:
                    retries += 1
                    continue

                tweets = self.parse_tweets(html)
                if not tweets:
                    print(f"No tweets found on page {page}. Stopping.")
                    break

                all_tweets.extend(tweets)
                page += 1

                # small random delay
                time.sleep(self.delay + random.uniform(0, 2))

            except Exception as e:
                print(f"Error scraping page {page}: {e}")
                retries += 1
                time.sleep(5)

        print(f"Found {len(all_tweets)} tweets from {username}")
        return all_tweets
