from solution import *

def test_find_pair_with_sum():
    assert find_pair_with_sum([2, 7, 11, 15], 9) == [0, 1]
    assert find_pair_with_index([3, 2, 4], 6) == [1, 2]
    assert find_pair_with_index([3, 3], 6) == [0, 1]
    assert find_pair_with_index([1, 2, 3, 4, 5], 10) == []
    assert find_pair_with_sum([], 10) == []

def find_pair_with_index(nums, k):
    return find_pair_with_sum(nums, k)