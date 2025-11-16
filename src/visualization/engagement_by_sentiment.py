# src/visualization/engagement_by_sentiment.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

os.makedirs("reports", exist_ok=True)
df = pd.read_csv("data/processed/sentiment_tweets.csv")

# Convert engagement columns to numeric if present
for col in ["likes", "retweets", "replies"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)
    else:
        df[col] = 0

label_col = "sentiment_label" if "sentiment_label" in df.columns else "sentiment"

avg = df.groupby(label_col)[["likes","retweets","replies"]].mean().reset_index()

# Melt for seaborn
melted = avg.melt(id_vars=label_col, var_name="metric", value_name="average")

plt.figure(figsize=(8,5))
sns.barplot(data=melted, x=label_col, y="average", hue="metric")
plt.title("Average Engagement by Sentiment")
plt.xlabel("Sentiment")
plt.ylabel("Average count")
plt.tight_layout()
out_path = "reports/engagement_by_sentiment.png"
plt.savefig(out_path, dpi=200, bbox_inches="tight")
plt.show()

print(f"Saved plot to {out_path}")
print(avg)
