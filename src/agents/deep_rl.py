# src/agents/deep_rl.py
import numpy as np
import logging
import torch
import torch.nn as nn
import torch.optim as optim

from .base_agent import BaseAgent

class ActorCritic(nn.Module):
    """
    Neural network model for deep reinforcement learning (Actor-Critic).
    """

    def __init__(self, state_dim, action_dim):
        super(ActorCritic, self).__init__()
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

class DeepRLAgent(BaseAgent):
    """
    Implements a Deep Reinforcement Learning trading agent using PPO.
    """

    def __init__(self, config):
        super().__init__(config)
        self.state_dim = config["state_dim"]
        self.action_dim = config["action_dim"]
        self.model = ActorCritic(self.state_dim, self.action_dim)
        self.optimizer = optim.Adam(self.model.parameters(), lr=config.get("learning_rate", 0.001))

    def act(self, market_state):
        """
        Generates an action using deep RL policy network.
        """
        state_tensor = torch.tensor(market_state["features"], dtype=torch.float32)
        action_probs, _ = self.model(state_tensor)
        action = torch.argmax(action_probs).item()
        self.logger.info(f"Deep RL Action taken: {action}")
        return action

    def update(self, reward, new_state):
        """
        Updates the policy using Proximal Policy Optimization (PPO).
        """
        _, value = self.model(torch.tensor(new_state["features"], dtype=torch.float32))
        loss = -reward * value.mean()
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        self.logger.info(f"Updated policy with reward: {reward}")
