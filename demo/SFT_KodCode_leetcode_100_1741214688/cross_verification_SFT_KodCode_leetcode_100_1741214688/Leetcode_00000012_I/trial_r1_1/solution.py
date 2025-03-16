def maxProfitWithTransactionFee(prices: List[int], fee: int) -> int:
    if len(prices) < 2:
        return 0
    
    hold = -prices[0]
    unhold = 0
    
    for price in prices[1:]:
        new_hold = max(hold, unhold - price)
        new_unhold = max(unhold, hold + price - fee)
        
        hold, unhold = new_hold, new_unhold
    
    return unhold