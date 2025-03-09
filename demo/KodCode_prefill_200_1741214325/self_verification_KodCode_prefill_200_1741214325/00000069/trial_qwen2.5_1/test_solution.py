from solution import *

from solution import count_trailing_zeros

def test_trailing_zeros_grade():
    assert count_trailing_zeros(1002000) == 3
    assert count_trailing_zeros(10500) == 2
    assert count_trailing_zeros(100005) == 1
    assert count_trailing_zeros(123) == 0
    assert count_trailing_zeros(0) == 1
    assert count_trailing_zeros(10000000000000000000) == 19