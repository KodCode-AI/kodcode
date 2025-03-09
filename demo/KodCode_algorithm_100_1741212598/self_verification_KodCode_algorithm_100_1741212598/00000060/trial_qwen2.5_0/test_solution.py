from solution import *

import pytest
from solution import diophantine_all_values

def test_diophantine_all_values():
    # Example 1
    a, b, c, upper_limit = 2, 3, 5, 5
    expected = [(-5, 5), (-4, 3), (-3, 1), (1, -4), (3, -2), (5, -1)]
    assert sorted(diophantine_all_values(a, b, c, upper_limit)) == sorted(expected)
    
    # Example 2
    a, b, c, upper_limit = 6, 9, 3, 10
    expected = []
    assert diophantine_all_values(a, b, c, upper_limit) == expected

    # Additional tests
    a, b, c, upper_limit = 1, 1, 2, 2
    expected = [(1, 1)]
    assert sorted(diophantine_all_values(a, b, c, upper_limit)) == sorted(expected)

    a, b, c, upper_limit = 5, 7, 35, 5
    expected = [(-5, 5), (0, 5), (5, 5)]
    assert sorted(diophantine_all_values(a, b, c, upper_limit)) == sorted(expected)

    a, b, c, upper_limit = 10, 15, 20, 3
    expected = []
    assert diophantine_all_values(a, b, c, upper_limit) == expected

    a, b, c, upper_limit = 13, 8, 52, 4
    expected = [(-4, 3), (0, 7), (4, 11)]
    assert sorted(diophantine_all_values(a, b, c, upper_limit)) == sorted(expected)

    a, b, c, upper_limit = 9, 9, 27, 5
    expected = [(-3, 1), (0, 3), (3, 5)]
    assert sorted(diophantine_all_values(a, b, c, upper_limit)) == sorted(expected)

    a, b, c, upper_limit = 7, 11, 35, 6
    expected = [(-5, 0), (-2, 2), (1, 2), (4, 0)]
    assert sorted(diophantine_all_values(a, b, c, upper_limit)) == sorted(expected)