# src/fundamental_analysis/macro_indicator.py
import numpy as np
import logging
import pandas as pd
from sklearn.linear_model import LinearRegression

class MacroIndicatorAnalysis:
    """
    Uses statistical models to analyze macroeconomic indicators (GDP, inflation, interest rates)
    for market impact and predictive analysis.
    """

    def __init__(self, data):
        self.data = data
        self.model = LinearRegression()
        self.logger = logging.getLogger("MacroIndicatorAnalysis")
        self.logger.setLevel(logging.INFO)

    def train(self):
        """
        Trains linear regression model to estimate impact of macroeconomic factors on asset prices.
        """
        X = self.data[["GDP", "Inflation", "Interest Rate"]]
        y = self.data["Market Return"]
        self.model.fit(X, y)
        self.logger.info("Macroeconomic model trained.")

    def predict_market_impact(self, new_data):
        """
        Predicts expected market impact based on macroeconomic conditions.
        """
        predicted_impact = self.model.predict(new_data[["GDP", "Inflation", "Interest Rate"]])
        self.logger.info(f"Predicted Market Impact: {predicted_impact}")
        return predicted_impact
