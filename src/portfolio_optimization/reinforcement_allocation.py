# src/portfolio_optimization/reinforcement_allocation.py
import numpy as np
import logging
import torch
import torch.nn as nn
import torch.optim as optim

class RLPortfolioOptimizer(nn.Module):
    """
    Implements reinforcement learning-based portfolio allocation.
    """

    def __init__(self, state_dim, action_dim):
        super(RLPortfolioOptimizer, self).__init__()
        self.actor = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, action_dim),
            nn.Softmax(dim=-1)
        )
        self.critic = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 1)
        )

    def forward(self, state):
        return self.actor(state), self.critic(state)

class RLPortfolioAgent:
    """
    Reinforcement Learning agent for adaptive portfolio allocation.
    """

    def __init__(self, config):
        self.state_dim = config["state_dim"]
        self.action_dim = config["action_dim"]
        self.model = RLPortfolioOptimizer(self.state_dim, self.action_dim)
        self.optimizer = optim.Adam(self.model.parameters(), lr=config.get("learning_rate", 0.001))
        self.logger = logging.getLogger("RLPortfolioAgent")
        self.logger.setLevel(logging.INFO)

    def act(self, market_state):
        """
        Generates portfolio allocation strategy using RL.
        """
        state_tensor = torch.tensor(market_state["features"], dtype=torch.float32)
        action_probs, _ = self.model(state_tensor)
        allocation = torch.argmax(action_probs).item()
        self.logger.info(f"Portfolio Allocation Decision: {allocation}")
        return allocation

    def update(self, reward, new_state):
        """
        Updates policy using reinforcement learning.
        """
        _, value = self.model(torch.tensor(new_state["features"], dtype=torch.float32))
        loss = -reward * value.mean()
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        self.logger.info(f"Updated portfolio strategy with reward: {reward}")
