def maxProfitWithTransactionFee(prices: List[int], fee: int) -> int:
    n = len(prices)
    if n < 2:
        return 0
    
    hold = -prices[0]
    not_hold = 0
    
    for i in range(1, n):
        new_hold = max(hold, not_hold - prices[i])
        new_not_hold = max(not_hold, hold + prices[i] - fee)
        hold, not_hold = new_hold, new_not_hold
    
    return not_hold