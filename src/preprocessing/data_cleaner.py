import pandas as pd
import re
import emoji
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import os

# Download NLTK data if missing
nltk.download('punkt')
nltk.download('stopwords')

def clean_text(text):
    """Clean tweet text by removing URLs, mentions, emojis, and stopwords."""
    if not isinstance(text, str):
        return ""

    # Remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)

    # Remove mentions
    text = re.sub(r"@\w+", "", text)

    # Remove hashtags (keep the word)
    text = re.sub(r"#", "", text)

    # Remove emojis
    text = emoji.replace_emoji(text, replace="")

    # Lowercase
    text = text.lower()

    # Remove punctuation & numbers
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # Tokenize
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words]

    return " ".join(tokens)

# Paths
INPUT_FILE = "data/raw/all_tweets_combined.csv"
OUTPUT_FILE = "data/processed/cleaned_tweets.csv"

if __name__ == "__main__":
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Input file not found: {INPUT_FILE}")
        exit()

    print("📥 Loading:", INPUT_FILE)
    df = pd.read_csv(INPUT_FILE)

    # Clean the 'text' column from the scraper
    df["cleaned_text"] = df["text"].apply(clean_text)

    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")
    print("\n✅ Cleaned tweets saved to:", OUTPUT_FILE)
