def maxProfitWithTransactionFee(prices: list, fee: int) -> int:
    """
    Calculate the maximum profit you can achieve from trading a stock with a transaction fee.
    """
    n = len(prices)
    if n < 2:
        return 0
    
    # Initialize variables to keep track of the maximum profit when we hold and when we do not hold a stock
    hold = -prices[0]  # Assume we buy the stock on the first day
    not_hold = 0       # No stock in hand
    
    for i in range(1, n):
        # If we decide to buy or keep the stock
        hold = max(hold, not_hold - prices[i])
        # If we decide to sell the stock
        not_hold = max(not_hold, hold + prices[i] - fee)
    
    return not_hold