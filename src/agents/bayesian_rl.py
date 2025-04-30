# src/agents/bayesian_rl.py
import numpy as np
import logging
from scipy.stats import norm

from .base_agent import BaseAgent

class BayesianRLAgent(BaseAgent):
    """
    Implements a Bayesian Reinforcement Learning trading agent.
    Incorporates uncertainty estimation to improve trade execution strategies.
    """

    def __init__(self, config):
        super().__init__(config)
        self.alpha = config.get("alpha", 0.05)  # Bayesian learning rate
        self.prior_mean = config.get("prior_mean", 0)
        self.prior_variance = config.get("prior_variance", 1)

    def act(self, market_state):
        """
        Generates an action based on market observations with Bayesian confidence.
        """
        mean_return = np.mean(market_state["returns"])
        uncertainty = norm.ppf(1 - self.alpha, loc=self.prior_mean, scale=np.sqrt(self.prior_variance))

        action = "BUY" if mean_return > uncertainty else "SELL"
        self.logger.info(f"Action taken: {action} with uncertainty threshold: {uncertainty}")
        return action

    def update(self, reward, new_state):
        """
        Updates the agent's Bayesian posterior distribution.
        """
        self.prior_mean = (self.prior_mean + reward) / 2
        self.prior_variance = (self.prior_variance + np.var(new_state["returns"])) / 2
        self.logger.info(f"Updated Bayesian parameters: Mean={self.prior_mean}, Variance={self.prior_variance}")
