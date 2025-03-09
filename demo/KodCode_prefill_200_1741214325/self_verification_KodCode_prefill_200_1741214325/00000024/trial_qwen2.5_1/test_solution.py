from solution import *

from solution import count_paths

def test_count_paths_small_grid():
    assert count_paths(2, 2) == 2

def test_count_paths_medium_grid():
    assert count_paths(3, 3) == 6
    assert count_paths(4, 3) == 10
    assert count_paths(3, 4) == 10

def test_count_paths_large_grid():
    assert count_paths(10, 10) == 184756

def test_count_paths_with_m_equal_n():
    for i in range(1, 11):
        assert count_paths(i, i) == (2 * i - 2) // 2 + 1