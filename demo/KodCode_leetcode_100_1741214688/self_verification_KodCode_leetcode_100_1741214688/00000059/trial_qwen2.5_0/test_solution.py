from solution import *

def test_max_absolute_difference():
    assert max_absolute_difference([1, 2, 3, 4], [2, 1, 4, 3]) == 10
    assert max_absolute_difference([1, 2, 3, 4], [1, 2, 3, 4]) == 8
    assert max_absolute_difference([1, 2, 3, 4], [4, 3, 2, 1]) == 10
    assert max_absolute_difference([1, 2, 4, 5], [2, 1, 5, 4]) == 10
    assert max_absolute_difference([4, 2, 3, 1], [7, 5, 11, 2]) == 20