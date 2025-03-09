from solution import *

import pytest

def test_simple_case():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 3
    assert find_smallest_path(grid, k) == [1, 2, 3]

def test_more_complex():
    grid = [[5, 9, 3], [4, 1, 6], [7, 8, 2]]
    k = 4
    assert find_smallest_path(grid, k) == [1, 3, 2, 6]

def test_large_k():
    grid = [[10], [11], [12]]
    k = 3
    assert find_smallest_path(grid, k) == [10, 11, 12]

def test (*((["[1, 2, 3], [4, 5, 6], [7, 8, 9]", 3], ['[1, 2, 3], [4, 5, 6], [7, 8, 9]", 3])),
           (["[5, 9, 3], [4, 1, 6], [7, 8, 2]", 4], ['[1, 3, 2, 6]'), (["[10], [11], [12]", 3], ['[10, 11, 12]')))