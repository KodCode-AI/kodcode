from typing import List

def maxProfitWithTransactionFee(prices: List[int], fee: int) -> int:
    if not prices:
        return 0
    prev_hold = -prices[0]
    prev_unhold = 0
    for price in prices[1:]:
        curr_hold = max(prev_hold, prev_unhold - price)
        curr_unhold = max(prev_unhold, prev_hold + price - fee)
        prev_hold, prev_unhold = curr_hold, curr_unhold
    return prev_unhold