import pandas as pd
import matplotlib.pyplot as plt
import os

# Load processed tweets with sentiment
df = pd.read_csv("data/processed/sentiment_tweets.csv")

# Ensure created_at is datetime
df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")

# Remove rows without valid dates
df = df.dropna(subset=["created_at"])

# Group by year + month
df["year_month"] = df["created_at"].dt.to_period("M")
tweet_counts = df["year_month"].value_counts().sort_index()

# Plot
plt.figure(figsize=(12, 6))
tweet_counts.plot(kind="bar")

plt.title("Tweet Frequency Over Time")
plt.xlabel("Month")
plt.ylabel("Number of Tweets")
plt.xticks(rotation=90)

# Save figure
output_path = "reports/figures/tweets_per_month.png"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.tight_layout()
plt.savefig(output_path, dpi=300)

print(f"📊 Saved tweets-per-month chart to: {output_path}")
plt.show()
