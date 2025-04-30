# src/risk_management/monte_carlo_sim.py
import numpy as np
import logging

class MonteCarloSimulator:
    """
    Simulates asset price movements using Monte Carlo methods.
    Used for risk assessment and trade strategy validation.
    """

    def __init__(self, num_simulations=10000, time_horizon=30):
        self.num_simulations = num_simulations
        self.time_horizon = time_horizon
        self.logger = logging.getLogger("MonteCarloSimulator")
        self.logger.setLevel(logging.INFO)

    def simulate(self, initial_price, volatility, drift):
        """
        Simulates asset price paths using Geometric Brownian Motion.
        """
        paths = np.zeros((self.num_simulations, self.time_horizon))
        paths[:, 0] = initial_price

        for t in range(1, self.time_horizon):
            random_shock = np.random.normal(drift, volatility, self.num_simulations)
            paths[:, t] = paths[:, t-1] * np.exp(random_shock)
        
        self.logger.info("Monte Carlo simulation completed.")
        return paths
