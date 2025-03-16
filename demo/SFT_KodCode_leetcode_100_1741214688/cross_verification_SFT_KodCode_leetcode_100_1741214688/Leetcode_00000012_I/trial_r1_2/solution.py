from typing import List

def maxProfitWithTransactionFee(prices: List[int], fee: int) -> int:
    if not prices:
        return 0
    prev_hold = -prices[0]
    prev_not_hold = 0
    for price in prices[1:]:
        current_hold = max(prev_hold, prev_not_hold - price)
        current_not_hold = max(prev_not_hold, prev_hold + price - fee)
        prev_hold, prev_not_hold = current_hold, current_not_hold
    return max(prev_hold, prev_not_hold)