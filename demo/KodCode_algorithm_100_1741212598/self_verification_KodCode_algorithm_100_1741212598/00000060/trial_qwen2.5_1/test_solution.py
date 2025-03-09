from solution import *

import pytest
from solution import diophantine_all_values

# Test case 1
def test_diophantine_all_values_positive():
    assert diophantine_all_values(2, 3, 5, 5) == [(-5, 5), (-4, 3), (-3, 1), (1, -4), (3, -2), (5, -1)]

# Test case 2
def test_diophantine_all_values_with_zero():
    assert diophantine_all_values(6, 9, 3, 10) == []

# Test case 3
def test_diophantine_all_values_mixed_sign():
    assert diophantine_all_values(1, -1, 0, 4) == [(-4, -4), (0, 0), (4, 4)]

# Test case 4
def test_diophantine_all_values_large_numbers():
    assert diophantine_all_values(7, 2, 100, 10) == [(10, 15), (27, 20), (44, 15), (61, 10), (78, 5)]

# Test case 5
def test_diophantine_all_values_no_solution():
    assert diophantine_all_values(11, 13, 25, 20) == []

# Test case 6
def test_diophantine_all_values_single_solution():
    assert diophantine_all_values(2, 1, 3, 10) == [(1, 1), (3, 1), (5, 1), (7, 1), (9, 1)]