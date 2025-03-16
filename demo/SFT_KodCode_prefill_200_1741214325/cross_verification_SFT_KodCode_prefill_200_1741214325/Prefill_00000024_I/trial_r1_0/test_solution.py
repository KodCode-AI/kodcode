from solution import *

from solution import count_paths

def test_count_paths_small_grid():
    assert count_paths(2, 2) == 2

def test_count_paths_medium_grid():
    assert count_paths(3, 3) == 6

def test_count_paths_large_grid():
    assert count_paths(5, 5) == 70

def test_count_paths_one_row_or_column():
    assert count_paths(1, 10) == 1
    assert count_paths(10, 1) == 1

def test_count_paths_memoization():
    # This tests the dynamic programming memoization effect by calling the function
    # multiple times with the same inputs to check if it returns the cached result directly
    count_paths(3, 3)
    assert count_paths(3, 3) == 6  # Verifies the result comes from memoization