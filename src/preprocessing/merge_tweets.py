import pandas as pd
import glob
import os

RAW_DIR = "data/raw/"
OUTPUT_FILE = "data/raw/all_tweets_combined.csv"

def merge_tweets():
    csv_files = glob.glob(os.path.join(RAW_DIR, "*_tweets.csv"))

    if not csv_files:
        print("❌ No tweet CSV files found in data/raw/")
        return

    all_dfs = []

    for file in csv_files:
        print(f"📥 Loading: {file}")
        df = pd.read_csv(file, encoding="utf-8")
        all_dfs.append(df)

    merged_df = pd.concat(all_dfs, ignore_index=True)

    print(f"\n🔢 Total tweets combined: {len(merged_df)}")

    merged_df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")
    print(f"✅ Merged file saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    merge_tweets()
