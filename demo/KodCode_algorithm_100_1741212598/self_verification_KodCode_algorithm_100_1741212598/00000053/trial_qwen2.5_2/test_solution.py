from solution import *

from solution import max_prize_fund

def test_max_prize_fund():
    assert max_prize_fund(4) == 10
    assert max_prize_fund(10) == 225
    assert max_prize_fund(1) == 1
    assert max_prize_fund(2) == 2

# Additional test cases
def test_more_turns():
    assert max_prize_fund(3) == 6
    assert max_prize_fund(5) == 55
    assert max_prize_fund(20) == 12870