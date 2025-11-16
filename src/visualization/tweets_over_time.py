import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/sentiment_tweets.csv")
df['created_at'] = pd.to_datetime(df['created_at'])

df_daily = df.resample('M', on='created_at').size()

plt.figure(figsize=(10,5))
df_daily.plot()

plt.title("Tweet Frequency Over Time")
plt.xlabel("Month")
plt.ylabel("Number of Tweets")

plt.savefig("reports/figures/tweets_over_time.png", dpi=300)
plt.show()
