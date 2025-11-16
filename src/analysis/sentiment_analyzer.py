import pandas as pd
from textblob import TextBlob
import os

INPUT_FILE = "data/processed/cleaned_tweets.csv"
OUTPUT_FILE = "data/processed/sentiment_tweets.csv"

def get_sentiment(text):
    if not isinstance(text, str) or text.strip() == "":
        return 0.0
    return TextBlob(text).sentiment.polarity

def get_label(score):
    if score > 0.05:
        return "positive"
    elif score < -0.05:
        return "negative"
    else:
        return "neutral"

if __name__ == "__main__":
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Missing input file: {INPUT_FILE}")
        exit()

    df = pd.read_csv(INPUT_FILE)

    print("🔍 Running sentiment analysis...")

    df["sentiment"] = df["cleaned_text"].apply(get_sentiment)
    df["sentiment_label"] = df["sentiment"].apply(get_label)

    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")

    print("\n✅ Sentiment analysis complete!")
    print("📁 Saved to:", OUTPUT_FILE)
    print(df.head(10))
