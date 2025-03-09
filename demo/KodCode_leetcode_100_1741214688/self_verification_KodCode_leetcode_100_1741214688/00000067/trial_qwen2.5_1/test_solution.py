from solution import *

def test_max_possible_value():
    assert max_possible_value([1, 3, 0, 0, 2], 3) == 6
    assert max_possible_value([1, 2, 3, 4, 5], 2) == 10
    assert max_possible_value([1, 1, 1, 1], 2) == 4
    assert max_possible_value([5, 5, 5, 5], 1) == 8
    assert max_possible_value([1, 2, 3], 2) == 4
    assert max_possible_value([10, 2, 3, 4, 5, 6, 7, 8, 9], 4) == 32