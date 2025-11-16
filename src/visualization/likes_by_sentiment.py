import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/sentiment_tweets.csv")

plt.figure(figsize=(8,5))
sns.boxplot(x="sentiment_label", y="like_count", data=df)

plt.title("Likes per Sentiment")
plt.xlabel("Sentiment")
plt.ylabel("Like Count")

plt.savefig("reports/figures/likes_by_sentiment.png", dpi=300)
plt.show()
