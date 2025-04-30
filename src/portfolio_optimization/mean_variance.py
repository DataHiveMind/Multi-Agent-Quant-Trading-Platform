# src/portfolio_optimization/mean_variance.py
import numpy as np
import logging
from scipy.optimize import minimize

class MeanVarianceOptimizer:
    """
    Implements Markowitz Mean-Variance Portfolio Optimization.
    """

    def __init__(self, expected_returns, covariance_matrix, risk_tolerance=1.0):
        self.expected_returns = expected_returns
        self.covariance_matrix = covariance_matrix
        self.risk_tolerance = risk_tolerance
        self.logger = logging.getLogger("MeanVarianceOptimizer")
        self.logger.setLevel(logging.INFO)

    def optimize_portfolio(self):
        """
        Computes the optimal portfolio allocation using mean-variance optimization.
        """

        num_assets = len(self.expected_returns)
        initial_weights = np.ones(num_assets) / num_assets

        def objective(weights):
            return -np.dot(weights, self.expected_returns) + self.risk_tolerance * np.dot(weights.T, np.dot(self.covariance_matrix, weights))

        constraints = {"type": "eq", "fun": lambda w: np.sum(w) - 1}
        bounds = [(0, 1) for _ in range(num_assets)]

        result = minimize(objective, initial_weights, method="SLSQP", bounds=bounds, constraints=constraints)

        self.logger.info(f"Optimized Portfolio Weights: {result.x}")
        return result.x
