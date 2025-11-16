import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re
import os
from nltk.corpus import stopwords
import nltk

# download nltk stopwords if not already
nltk.download('stopwords')

def load_data():
    path = "data/processed/cleaned_tweets.csv"
    if not os.path.exists(path):
        print(f"❌ File not found: {path}")
        return None
    return pd.read_csv(path)

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', '', text)  # remove urls
    text = re.sub(r'[^a-z\s]', '', text)  # keep only letters
    return text

def get_most_common_words(df, top_n=20):
    stop_words = set(stopwords.words('english'))

    all_words = []
    for text in df['cleaned_text'].dropna():
        text = preprocess_text(text)
        words = [w for w in text.split() if w not in stop_words and len(w) > 2]
        all_words.extend(words)

    return Counter(all_words).most_common(top_n)

def plot_most_common_words(word_counts):
    words = [w[0] for w in word_counts]
    counts = [w[1] for w in word_counts]

    plt.figure(figsize=(12, 6))
    plt.bar(words, counts)
    plt.xticks(rotation=45, ha='right')
    plt.title("Most Common Words in Tweets")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.tight_layout()

    # save to reports
    save_path = "reports/most_common_words.png"
    plt.savefig(save_path)
    plt.close()
    print(f"✅ Saved plot to {save_path}")

def main():
    df = load_data()
    if df is None:
        return

    if "cleaned_text" not in df.columns:
        print("❌ 'cleaned_text' column missing in cleaned_tweets.csv")
        return

    print("📊 Generating most common words visualization...")
    word_counts = get_most_common_words(df)
    plot_most_common_words(word_counts)


if __name__ == "__main__":
    main()
