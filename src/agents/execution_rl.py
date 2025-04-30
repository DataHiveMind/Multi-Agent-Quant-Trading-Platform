# src/agents/execution_rl.py
import numpy as np
import logging

from .base_agent import BaseAgent

class ExecutionRLAgent(BaseAgent):
    """
    Implements reinforcement learning for adaptive trade execution.
    Learns optimal placement based on latency, market volatility, and order book dynamics.
    """

    def __init__(self, config):
        super().__init__(config)
        self.trade_threshold = config.get("trade_threshold", 0.02)
    
    def act(self, market_state):
        """
        Determines optimal execution strategy given real-time order book dynamics.
        """
        spread = market_state["ask"] - market_state["bid"]
        action = "AGGRESSIVE_BUY" if spread < self.trade_threshold else "PASSIVE_BUY"
        self.logger.info(f"Execution RL decided action: {action}, Spread: {spread}")
        return action

    def update(self, reward, new_state):
        """
        Adjusts execution strategy based on market shifts.
        """
        self.trade_threshold = max(0.01, self.trade_threshold + reward * 0.01)
        self.logger.info(f"Updated execution threshold: {self.trade_threshold}")
