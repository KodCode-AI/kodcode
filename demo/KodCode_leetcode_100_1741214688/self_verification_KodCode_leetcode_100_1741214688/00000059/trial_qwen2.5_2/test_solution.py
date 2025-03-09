from solution import *

from solution import max_absolute_sum

def test_max_absolute_sum():
    assert max_absolute_sum([1, 2, 3, 4], [2, 1, 4, 3]) == 10
    assert max_absolute_sum([1, 2, 4, 5], [2, 1, 4, 4]) == 10
    assert max_absolute_sum([1, 1, 1, 1], [4, 4, 4, 4]) == 12
    assert max_absolute_sum([1], [1]) == 0
    assert max_absolute_sum([1, 7], [4, 3]) == 8
    assert max_absolute_sum([6, 12, 8, 10, 2, 5], [7, 1, 4, 8, 2, 9]) == 26

# Test with different random inputs
import random
def test_random():
    for _ in range(10):
        nums1 = [random.randint(1, 100) for _ in range(10)]
        nums2 = [random.randint(1, 100) for _ in range(10)]
        assert max_absolute_sum(nums1, nums2) == max_absolute_sum(sorted(nums1, reverse=True), sorted(nums2))