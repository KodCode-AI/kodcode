from solution import *

def test_find_pair_indices():
    assert find_pair_indices([1, 3, 5, 7, 9], 12) == [1, 3] or [3, 1]
    assert find_pair_indices([2, 4, 6, 8, 10], 15) == [2, 3] or [3, 2]
    assert find_pair_indices([5, 10, 3, 7], 13) == [1, 3] or [3, 1]
    assert find_pair_indices([1, 2, 3, 4], 8) == []
    assert find_pair_indices([0, 1, 4, 9, 13, 18], 15) == [0, 3] or [3, 0]
    assert find_pair_indices([11, 22, 33, 44], 66) == [0, 2] or [2, 0]

def test_find_pair_indices_negative():
    assert find_pair_indices([1, 2, -3, -2], -1) == [1, 2] or [2, 1]
    assert find_pair_indices([-5, 1, 2, -3, 4], 2) == [2, 3] or [3, 2]
    assert find_pair_indices([-14, 5, 8, 2, 7, 5], 10) == [1, 5] or [5, 1]
    assert find_pair_indices([-5, -1, 0, 1, 3, 9], 4) == [3, 4] or [4, 3]