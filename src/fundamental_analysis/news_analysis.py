# src/fundamental_analysis/news_analysis.py
import numpy as np
import logging
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class NewsSentimentAnalysis:
    """
    Analyzes real-time financial news sentiment using NLP for trading decisions.
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.analyzer = SentimentIntensityAnalyzer()
        self.logger = logging.getLogger("NewsSentimentAnalysis")
        self.logger.setLevel(logging.INFO)

    def fetch_news(self, query="markets"):
        """
        Retrieves financial news articles using an API (e.g., Alpha Vantage, NewsAPI).
        """
        url = f"https://newsapi.org/v2/everything?q={query}&apiKey={self.api_key}"
        response = requests.get(url)
        articles = response.json().get("articles", [])
        self.logger.info(f"Fetched {len(articles)} news articles.")
        return [article["title"] + " " + article["description"] for article in articles]

    def analyze_news_sentiment(self, news_texts):
        """
        Computes aggregated sentiment scores for financial news.
        """
        sentiment_scores = [self.analyzer.polarity_scores(text)["compound"] for text in news_texts]
        avg_sentiment = np.mean(sentiment_scores)
        self.logger.info(f"Average News Sentiment Score: {avg_sentiment}")
        return avg_sentiment
