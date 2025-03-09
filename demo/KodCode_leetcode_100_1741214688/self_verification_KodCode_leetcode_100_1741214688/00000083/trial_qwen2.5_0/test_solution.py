from solution import *

def test_k_smallest_abs_diff():
    assert k_smallest_abs_diff([1, 3, -1], 2) == [0, 2]
    assert k_smallest_abs_diff([1, -1], 1) == [0]
    assert k_smallest_abs_diff([4, 2, 8, 3, 10, 4], 5) == [1, 2, 3, 4, 5]
    assert k_smallest_abs_diff([2, 4, 8, 4, 2], 2) == [0, 2]
    assert k_smallest_abs_diff([7, 5, 4, 3], 3) == [1, 2, 3]