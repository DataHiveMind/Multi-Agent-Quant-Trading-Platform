# src/fundamental_analysis/earnings_sentiment.py
import numpy as np
import logging
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class EarningsSentimentAnalyzer:
    """
    Uses NLP to extract sentiment scores from earnings call transcripts.
    """

    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
        self.logger = logging.getLogger("EarningsSentimentAnalyzer")
        self.logger.setLevel(logging.INFO)

    def analyze_sentiment(self, transcript):
        """
        Computes sentiment score for given earnings call transcript.
        """
        sentiment_score = self.analyzer.polarity_scores(transcript)["compound"]
        self.logger.info(f"Sentiment score: {sentiment_score}")
        return sentiment_score
