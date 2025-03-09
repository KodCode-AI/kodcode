from solution import *

import math
from solution import max_prize_fund

def test_max_prize_fund():
    assert max_prize_fund(1) == 1, "Test case num_turns=1 failed"
    assert max_prize_fund(4) == 10, "Test case num_turns=4 failed"
    assert max_prize_fund(10) == 225, "Test case num_turns=10 failed"
    assert max_prize_fund(5) == 31, "Test case num_turns=5 failed"
    assert max_prize_fund(2) == 3, "Test case num_turns=2 failed"
    assert max_prize_fund(3) == 7, "Test case num_turns=3 failed"

def test_combinations():
    assert comb(5, 2) == 10, "Comb(5, 2) test failed"
    assert comb(6, 3) == 20, "Comb(6, 3) test failed"
    assert comb(8, 4) == 70, "Comb(8, 4) test failed"

test_max_prize_fund()
test_combinations()