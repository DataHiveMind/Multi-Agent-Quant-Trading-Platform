# src/agents/factor_models.py
import numpy as np
import logging
from sklearn.linear_model import Ridge

class FactorModel:
    """
    Implements a machine learning-driven factor investing model.
    Uses Ridge Regression for selecting the best predictive factors.
    """

    def __init__(self, factor_data):
        self.factor_data = factor_data
        self.model = Ridge(alpha=1.0)
        self.logger = logging.getLogger("FactorModel")
        self.logger.setLevel(logging.INFO)

    def train(self):
        """
        Trains Ridge Regression model on historical factor data.
        """
        X = self.factor_data["features"]
        y = self.factor_data["returns"]
        self.model.fit(X, y)
        self.logger.info("Factor model trained.")

    def predict(self, new_data):
        """
        Predicts expected returns using learned factor model.
        """
        predicted_return = self.model.predict(new_data["features"])
        self.logger.info(f"Predicted return: {predicted_return}")
        return predicted_return
