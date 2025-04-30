# src/portfolio_optimization/black_litterman.py
import numpy as np
import logging

class BlackLittermanModel:
    """
    Implements the Black-Litterman portfolio optimization model.
    Adjusts asset allocation based on Bayesian priors and investor sentiment.
    """

    def __init__(self, prior_returns, market_cap_weights, confidence_matrix):
        self.prior_returns = prior_returns
        self.market_cap_weights = market_cap_weights
        self.confidence_matrix = confidence_matrix
        self.logger = logging.getLogger("BlackLittermanModel")
        self.logger.setLevel(logging.INFO)

    def optimize(self):
        """
        Adjusts asset allocation based on market priors and investor confidence.
        """
        eq_returns = np.dot(self.market_cap_weights, self.prior_returns)
        adjusted_returns = eq_returns + np.dot(self.confidence_matrix, (self.prior_returns - eq_returns))

        self.logger.info("Portfolio optimization completed.")
        return adjusted_returns
