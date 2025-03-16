from solution import *

def test_maxProfitWithTransactionFee():
    assert maxProfitWithTransactionFee([1, 3, 2, 8, 4, 9], 2) == 8, "Test case 1 failed"
    assert maxProfitWithTransactionFee([1, 3, 7, 5, 10, 3], 3) == 6, "Test case 2 failed"
    assert maxProfitWithTransactionFee([1], 0) == 0, "Test case 3 failed"
    assert maxProfitWithTransactionFee([1, 2, 3, 4, 5], 1) == 3, "Test case 4 failed"
    assert maxProfitWithTransactionFee([7, 6, 4, 3, 1], 2) == 0, "Test case 5 failed"

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])