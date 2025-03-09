from solution import *

def test_maxProfitWithTransactionFee():
    assert maxProfitWithTransactionFee([1, 3, 2, 8, 4, 9], 2) == 8
    assert maxProfitWithTransactionFee([1, 3, 7, 5, 10, 3], 3) == 6
    assert maxProfitWithTransactionFee([1, 2, 3, 0, 2], 1) == 2
    assert maxProfitWithTransactionFee([10], 0) == 0
    assert maxProfitWithTransactionFee([5, 6, 1, 5], 2) == 3

test_maxProfitWithTransactionFee()