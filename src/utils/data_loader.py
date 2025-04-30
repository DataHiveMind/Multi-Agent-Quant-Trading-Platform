# src/utils/data_loader.py
import pandas as pd
import numpy as np
import logging

class DataLoader:
    """
    Handles data ingestion, preprocessing, and feature engineering.
    """

    def __init__(self, data_path):
        self.data_path = data_path
        self.logger = logging.getLogger("DataLoader")
        self.logger.setLevel(logging.INFO)

    def load_data(self):
        """
        Loads financial data from a CSV file.
        """
        try:
            df = pd.read_csv(self.data_path)
            self.logger.info(f"Data loaded from {self.data_path}. Shape: {df.shape}")
            return df
        except Exception as e:
            self.logger.error(f"Error loading data: {e}")
            return None

    def preprocess(self, df):
        """
        Cleans data by handling missing values and outliers.
        """
        df.fillna(method="ffill", inplace=True)
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df.dropna(inplace=True)
        
        self.logger.info("Data preprocessing completed.")
        return df
