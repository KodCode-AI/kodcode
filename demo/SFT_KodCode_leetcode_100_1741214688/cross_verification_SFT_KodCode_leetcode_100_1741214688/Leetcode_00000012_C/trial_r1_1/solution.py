def maxProfitWithTransactionFee(prices: List[int], fee: int) -> int:
    if not prices:
        return 0
    
    hold = -prices[0]  # Assume we buy on the first day
    not_hold = 0       # No stock in hand
    
    for price in prices[1:]:
        new_hold = max(hold, not_hold - price)
        new_not_hold = max(not_hold, hold + price - fee)
        hold, not_hold = new_hold, new_not_hold
    
    return max(hold, not_hold)