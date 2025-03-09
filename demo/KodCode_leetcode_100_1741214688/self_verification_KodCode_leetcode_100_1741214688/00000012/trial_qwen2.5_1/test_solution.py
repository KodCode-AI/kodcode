from solution import *

from typing import List
from solution import maxProfitWithTransactionFee

def test_maxProfitWithTransactionFee():
    assert maxProfitWithTransactionFee([1, 3, 2, 8, 4, 9], 2) == 8
    assert maxProfitWithTransactionFee([1, 3, 7, 5, 10, 3], 3) == 6
    assert maxProfitWithTransactionFee([5, 2, 6, 3, 1, 4], 0) == 4
    assert maxProfitWithTransactionFee([1], 2) == 0
    assert maxProfitWithTransactionFee([1, 3, 2, 8, 4, 9], 0) == 10
    assert maxProfitWithTransactionFee([1, 3, 7, 5, 10, 3], 2) == 5

# Test with an empty prices list
assert maxProfitWithTransactionFee([], 2) == 0

# Test with a single element in prices
assert maxProfitWithTransactionFee([100], 2) == 0

# Test with a large number of prices
large_prices = list(range(1, 50000))
assert maxProfitWithTransactionFee(large_prices, 10) == 0  # No profit if the transaction fee is greater than the price difference