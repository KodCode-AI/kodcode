from solution import *

def test_custom_comparator():
    def helper(arr):
        comparator = CustomComparator(arr)
        comparator.sort()
        even_indices = sorted(arr[::2])
        odd_indices = sorted(arr[1::2], reverse=True)
        expected = [even if i % 2 == 0 else odd for i, (even, odd) in enumerate(zip(even_indices, odd_indices + arr[-1:] * (len(arr) % 2)))]
        assert comparator.get_result() == expected

    helper([4, 1, 3, 2, 6, 5])
    helper([10, 15, 2, 5, 8, 7, 6, 4])
    helper([3, 1, 4, 1, 5, 9, 2, 6])
    helper([11, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    helper([])
    helper([1])

import pytest

if __name__ == "__main__":
    pytest.main()