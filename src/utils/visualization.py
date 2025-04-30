# src/utils/visualization.py
import matplotlib.pyplot as plt
import seaborn as sns
import logging

class Visualization:
    """
    Creates visual analytics for trading and financial research.
    """

    def __init__(self):
        self.logger = logging.getLogger("Visualization")
        self.logger.setLevel(logging.INFO)

    def plot_price_series(self, df, title="Price Series"):
        """
        Plots historical price series.
        """
        plt.figure(figsize=(12, 6))
        sns.lineplot(x=df.index, y=df["Close"])
        plt.title(title)
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.show()

        self.logger.info("Price series plotted.")
