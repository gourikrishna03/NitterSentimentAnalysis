import pandas as pd
from .nitter_scraper import NitterScraper

class DataCollector:
    def __init__(self, output_path="data/raw/tweets.csv"):
        self.scraper = NitterScraper()
        self.output_path = output_path

    def collect_users(self, users):
        all_data = []

        for user in users:
            print(f"\nCollecting tweets for: {user}")
            user_tweets = self.scraper.scrape_user(user)

            for t in user_tweets:
                t["username"] = user
                all_data.append(t)

        df = pd.DataFrame(all_data)
        df.to_csv(self.output_path, index=False)
        print(f"\n✅ Saved collected tweets to {self.output_path}")

        return df
