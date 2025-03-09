from solution import *

def test_find_pairs_with_sum():
    assert find_pairs_with_sum([1, 3, 2, 2], 4) == [(1, 3), (2, 2)]
    assert find_pairs_with_sum([1, 5, 7, -1], 6) == [(-1, 7), (1, 5)]
    assert find_pairs_with_sum([1, 2, 3, 7, -2, -7, 1], 5) == [(-2, 7), (1, 4), (1, 4)]
    assert find_pairs_with_sum([], 4) == []
    assert find_pairs_with_sum([1, 2, 3, 4], 8) == []