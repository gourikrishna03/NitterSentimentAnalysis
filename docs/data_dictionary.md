📂 1. Raw Dataset (data/raw/*.csv)
Column Name	Description
tweet_id	Unique ID assigned to the tweet
username	The Twitter/X username scraped (e.g., ilyasut)
timestamp	Date & time of the tweet in ISO format (YYYY-MM-DD HH:MM:SS)
text	Raw tweet text including URLs, mentions, emojis
comments	Number of comments/replies on the tweet
retweets	Number of retweets
likes	Number of likes
urls	Comma-separated list of URLs extracted from tweet
is_retweet	Boolean flag indicating if tweet is a retweet
📂 2. Cleaned Dataset (data/processed/cleaned_tweets.csv)
Column Name	Description
tweet_id	Unique ID inherited from raw dataset
username	Original account name
timestamp	Cleaned timestamp
clean_text	Tweet text after removing URLs, emojis, punctuation, stopwords
word_count	Number of words in the cleaned tweet
is_retweet	Indicates if the tweet was originally a retweet
📂 3. Sentiment Dataset (data/processed/sentiment_tweets.csv)
Column Name	Description
tweet_id	Unique ID of the tweet
username	Account from which the tweet was scraped
timestamp	Tweet date
clean_text	Preprocessed tweet text
sentiment_score	VADER/TextBlob compound score
sentiment_label	Sentiment class (Positive / Neutral / Negative)
polarity	Polarity score (if using TextBlob)
subjectivity	Subjectivity score (if using TextBlob)
📁 4. Notes

All timestamps follow ISO format.

Cleaning removes URLs, emojis, HTML entities, and repeated spaces.

Sentiment scoring uses VADER or TextBlob, depending on your implementation.