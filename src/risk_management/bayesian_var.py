# src/risk_management/bayesian_var.py
import numpy as np
import logging
from scipy.stats import norm

class BayesianVaR:
    """
    Implements Bayesian Value-at-Risk (VaR) modeling for risk assessment.
    """

    def __init__(self, confidence_level=0.95):
        self.confidence_level = confidence_level
        self.logger = logging.getLogger("BayesianVaR")
        self.logger.setLevel(logging.INFO)

    def calculate_var(self, historical_returns):
        """
        Computes Bayesian VaR using probabilistic inference.
        """
        mean_return = np.mean(historical_returns)
        std_dev = np.std(historical_returns)
        
        var_value = norm.ppf(1 - self.confidence_level, loc=mean_return, scale=std_dev)
        self.logger.info(f"Computed Bayesian VaR: {var_value}")
        return var_value
