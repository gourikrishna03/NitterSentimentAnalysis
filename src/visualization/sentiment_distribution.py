# src/visualization/sentiment_distribution.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("reports", exist_ok=True)

df = pd.read_csv("data/processed/sentiment_tweets.csv")

# Safe column name handling
label_col = "sentiment_label" if "sentiment_label" in df.columns else "sentiment"

counts = df[label_col].value_counts().reindex(["positive","neutral","negative"], fill_value=0)

plt.figure(figsize=(6,4))
sns.barplot(x=counts.index, y=counts.values)
plt.title("Sentiment distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.tight_layout()
out_path = "reports/sentiment_distribution.png"
plt.savefig(out_path, dpi=200, bbox_inches="tight")
plt.show()

print(f"Saved plot to {out_path}")
print(counts)
