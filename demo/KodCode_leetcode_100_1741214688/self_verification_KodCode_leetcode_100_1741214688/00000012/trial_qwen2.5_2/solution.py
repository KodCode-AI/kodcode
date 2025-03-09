from typing import List

def maxProfitWithTransactionFee(prices: List[int], fee: int) -> int:
    """
    Calculates the maximum profit from trading stocks given the prices and a transaction fee.
    
    :param prices: List of daily stock prices.
    :param fee: Transaction fee for each transaction.
    :return: Maximum profit possible.
    """
    cash, hold = 0, -prices[0]  # cash: profit when not holding stock, hold: profit when holding stock
    
    for i in range(1, len(prices)):
        cash, hold = max(cash, hold + prices[i] - fee), max(hold, cash - prices[i])
    
    return cash