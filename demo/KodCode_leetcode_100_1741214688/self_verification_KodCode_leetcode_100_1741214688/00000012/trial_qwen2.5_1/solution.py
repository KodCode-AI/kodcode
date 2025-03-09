from typing import List

def maxProfitWithTransactionFee(prices: List[int], fee: int) -> int:
    """
    Returns the maximum profit that can be achieved from trading a stock given daily prices and a transaction fee.
    """
    n = len(prices)
    if n < 2:
        return 0
    
    # Initialize the states
    # hold: the maximum profit when holding a stock
    # not_hold: the maximum profit when not holding a stock
    hold, not_hold = -prices[0], 0
    
    for i in range(1, n):
        # Update the states
        hold = max(hold, not_hold - prices[i])
        not_hold = max(not_hold, hold + prices[i] - fee)
    
    return not_hold