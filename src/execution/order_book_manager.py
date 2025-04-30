# src/execution/order_book_manager.py
import numpy as np
import logging

class OrderBookManager:
    """
    Handles real-time market order book data processing and order tracking.
    """

    def __init__(self):
        self.order_book = {"bids": [], "asks": []}
        self.logger = logging.getLogger("OrderBookManager")
        self.logger.setLevel(logging.INFO)

    def update_order_book(self, bid_price, bid_size, ask_price, ask_size):
        """
        Updates the bid-ask spread with incoming market data.
        """
        self.order_book["bids"].append({"price": bid_price, "size": bid_size})
        self.order_book["asks"].append({"price": ask_price, "size": ask_size})

        self.logger.info(f"Order book updated: Bid={bid_price}({bid_size}), Ask={ask_price}({ask_size})")

    def get_spread(self):
        """
        Returns the bid-ask spread for market analysis.
        """
        if not self.order_book["bids"] or not self.order_book["asks"]:
            return None

        best_bid = max(self.order_book["bids"], key=lambda x: x["price"])
        best_ask = min(self.order_book["asks"], key=lambda x: x["price"])

        spread = best_ask["price"] - best_bid["price"]
        return spread
