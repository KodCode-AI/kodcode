from solution import *

``
import pytest

# Test cases
test_cases = [
    ([1, 2, 3, 4, 5], 1),
    ([5, 5, 5, 5, 5], 5),
    ([5, 5, 5, 5], 0),
    ([3], 3),
    ([], 0),
    ([1, 2, 3, 4], 0),
    ([-1, -5, 5, 1], 0),
    ([9, 9, 9, 9, 9], 9),
    ([1, 5, 10, 3], 1),
    ([-1, 0, 1], 0),
    (list(range(10, 0, -1)), 1),
    ([-1], 1),
    ([0, 0, 0, 1, 2, -4], 2),
    ([-1, -5, -10, -3], 3)
]

@pytest.mark.parametrize("numbers, expected", test_cases)
def test_find_min_difference(numbers, expected):
    assert find_min_difference(numbers) == expected