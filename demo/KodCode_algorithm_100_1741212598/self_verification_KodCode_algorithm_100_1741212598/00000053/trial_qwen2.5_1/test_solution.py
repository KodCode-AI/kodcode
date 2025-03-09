from solution import *

import pytest

def test_max_prize_fund():
    assert max_prize_fund(4) == 10
    assert max_prize_fund(10) == 225
    assert max_prize_fund(1) == 2
    assert max_prize_fund(2) == 3
    assert max_prize_fund(20) == 92378

def test_max_prize_fund_edge_cases():
    with pytest.raises(AssertionError):
        max_prize_fund(0)
    with pytest.raises(AssertionError):
        max_prize_fund(-5)
    with pytest.raises(AssertionError):
        max_prize_fund(21)

if __name__ == "__main__":
    pytest.main()