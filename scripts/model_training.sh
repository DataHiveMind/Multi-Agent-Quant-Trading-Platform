#!/bin/bash

echo "Starting model training..."

# Train Bayesian Reinforcement Learning Agent
python src/agents/bayesian_rl.py --train

# Train Deep RL Trading Agent
python src/agents/deep_rl.py --train

echo "Model training completed!"
