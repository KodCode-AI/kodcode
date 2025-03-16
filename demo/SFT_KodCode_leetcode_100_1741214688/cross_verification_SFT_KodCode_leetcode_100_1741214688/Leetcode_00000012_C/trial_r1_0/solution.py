def maxProfitWithTransactionFee(prices: list[int], fee: int) -> int:
    n = len(prices)
    if n < 2:
        return 0
    
    # Initialize variables to keep track of the maximum profit
    hold = -prices[0]  # Assume we buy the stock on the first day
    not_hold = 0       # No stock in hand initially
    
    for i in range(1, n):
        # Update the hold state to be the maximum of holding or buying today
        hold = max(hold, not_hold - prices[i])
        # Update the not_hold state to be the maximum of not holding or selling today after fee
        not_hold = max(not_hold, hold + prices[i] - fee)
    
    return not_hold