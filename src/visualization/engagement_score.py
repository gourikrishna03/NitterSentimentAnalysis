import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/sentiment_tweets.csv")
df["engagement"] = df["like_count"] + df["retweet_count"] + df["comment_count"]

plt.figure(figsize=(8,5))
sns.boxplot(x="sentiment_label", y="engagement", data=df)

plt.title("Engagement by Sentiment")
plt.xlabel("Sentiment")
plt.ylabel("Engagement Score")

plt.savefig("reports/figures/engagement_by_sentiment.png", dpi=300)
plt.show()
