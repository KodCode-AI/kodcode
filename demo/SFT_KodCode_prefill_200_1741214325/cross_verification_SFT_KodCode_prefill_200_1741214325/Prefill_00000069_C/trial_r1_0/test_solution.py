from solution import *

def test_count_trailing_zeros():
    assert count_trailing_zeros(1000) == 3
    assert count_trailing_zeros(123000) == 3
    assert count_trailing_zeros(123) == 0
    assert count_trailing_zeros(0) == 1