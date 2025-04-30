# src/risk_management/stress_testing.py
import numpy as np
import logging

class StressTester:
    """
    Simulates adverse market conditions for portfolio robustness testing.
    """

    def __init__(self, scenarios):
        self.scenarios = scenarios
        self.logger = logging.getLogger("StressTester")
        self.logger.setLevel(logging.INFO)

    def evaluate_portfolio(self, portfolio_returns):
        """
        Applies predefined stress scenarios to portfolio performance.
        """
        results = {}
        for scenario, shock in self.scenarios.items():
            stressed_returns = portfolio_returns * (1 + shock)
            results[scenario] = np.mean(stressed_returns)
            self.logger.info(f"Scenario '{scenario}': Mean Portfolio Return = {results[scenario]}")

        return results
