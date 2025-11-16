# AI Capstone Project – README

## 📌 Project Overview

This project performs **Twitter data scraping, cleaning, sentiment analysis, and visualization** using Selenium, Python, and NLP techniques.

The dataset consists of tweets from AI researchers and public figures, cleaned and processed for analysis. Final outputs include sentiment distributions, tweet frequency trends, and engagement metrics.

---

## 📁 Folder Structure

```
AI-CAPSTONE/
│
├── config/
│   └── config.yaml
│
├── data/
│   ├── raw/
│   │   ├── all_tweets_combined.csv
│   │   ├── geoffreyhinton_tweets.csv
│   │   ├── ilyasut_tweets.csv
│   │   └── karpathy_tweets.csv
│   │
│   └── processed/
│       ├── cleaned_tweets.csv
│       └── sentiment_tweets.csv
│
├── results/
│
├── reports/
│   ├── figures/
│   │   ├── engagement_by_sentiment.png
│   │   ├── likes_by_sentiment.png
│   │   ├── sentiment_distribution.png
│   │   ├── tweets_over_time.png
│   │   ├── tweets_per_month.png
│   │   └── most_common_words.png
│
├── docs/
│
├── notebooks/
│
├── outputs/
│
├── src/
│   ├── scraper/
│   │   ├── __init__.py
│   │   ├── nitter_scraper.py
│   │   └── data_collector.py
│   │
│   └── selenium_scraper.py
│
├── tests/
│
└── venv/
```

---

## 🚀 Features

* Automated **web scraping** using Selenium
* **Data cleaning**: removing URLs, emojis, punctuation, duplicates
* **Sentiment analysis** using VADER/TextBlob
* **Visual analytics** with Matplotlib + Seaborn
* Multi-user tweet collection for comparison
* Report-ready graphs stored in `reports/figures/`

---

## 🧩 Installation

```bash
pip install -r requirements.txt
```

For Selenium:

```bash
pip install selenium webdriver-manager
```

---

## ⚙️ How to Run

### 1. Run the Scraper

```bash
python src/selenium_scraper.py
```

### 2. Run Data Cleaning

Processes raw tweets into clean format.

```bash
python src/scraper/data_collector.py
```

### 3. Run Sentiment Analysis

Creates `sentiment_tweets.csv`.

```bash
python notebooks/sentiment_analysis.ipynb
```

### 4. Generate Visualizations

Plots will be saved automatically to:

```
reports/figures/
```

---

## 📊 Output Files

| File                        | Description                        |
| --------------------------- | ---------------------------------- |
| cleaned_tweets.csv          | Fully cleaned dataset              |
| sentiment_tweets.csv        | Tweets with sentiment labels       |
| sentiment_distribution.png  | Pie/Bar chart of sentiment classes |
| tweets_over_time.png        | Line graph of tweet timeline       |
| tweets_per_month.png        | Monthly tweet activity             |
| engagement_by_sentiment.png | Likes + retweets grouped           |
| most_common_words.png       | Word frequency chart               |

---

## 📚 References

* Python Official Documentation
* Pandas Documentation
* Selenium Documentation
* Publicly available interviews from AI researchers

---

## 👨‍💻 Author

Generated as part of the **AI Capstone Project**.
