from solution import *

from solution import find_pair_indices

def test_find_pair_indices():
    assert find_pair_indices([2, 7, 11, 15], 9) == [0, 1]
    assert find_pair_indices([3, 2, 4], 6) == [1, 2]
    assert find_pair_indices([3, 3], 6) == [0, 1]
    assert find_pair_indices([1, 2, 3], 7) == []
    assert find_pair_indices([0, 2, -2, 5, 1], 3) == [1, 3]
    assert find_pair_indices([1, 5, 9, 7], 10) == [0, 2]
    assert find_pair_indices([1, 5, 9, 7], 16) == [2, 3]
    assert find_pair_indices([], 5) == []
    assert find_pair_indices([1], 2) == []