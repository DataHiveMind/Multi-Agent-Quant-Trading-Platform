# src/agents/base_agent.py
from abc import ABC, abstractmethod
import numpy as np
import logging

class BaseAgent(ABC):
    """
    Abstract base class for all trading agents.
    Provides a common interface for implementing reinforcement learning agents and quant strategies.
    """

    def __init__(self, config):
        """
        Initialize the trading agent with configuration parameters.
        """
        self.config = config
        self.state = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)

    @abstractmethod
    def act(self, market_state):
        """
        Defines the agent's action given the current market state.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def update(self, reward, new_state):
        """
        Updates the agent's internal state based on received reward and new observations.
        """
        pass

    def reset(self):
        """
        Resets the agent's internal state for a new trading session.
        """
        self.state = None
        self.logger.info("Agent state reset.")

    def save_model(self, file_path):
        """
        Saves the agent's model parameters.
        """
        try:
            np.save(file_path, self.state)
            self.logger.info(f"Model saved to {file_path}")
        except Exception as e:
            self.logger.error(f"Failed to save model: {e}")

    def load_model(self, file_path):
        """
        Loads the agent's model parameters.
        """
        try:
            self.state = np.load(file_path)
            self.logger.info(f"Model loaded from {file_path}")
        except Exception as e:
            self.logger.error(f"Failed to load model: {e}")
