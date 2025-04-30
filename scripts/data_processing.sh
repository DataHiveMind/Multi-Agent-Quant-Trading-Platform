#!/bin/bash

echo "Starting data preprocessing..."

# Load data
python src/utils/data_loader.py --path datasets/market_data.csv

# Clean and preprocess
python src/utils/data_loader.py --preprocess

echo "Data preprocessing completed!"
