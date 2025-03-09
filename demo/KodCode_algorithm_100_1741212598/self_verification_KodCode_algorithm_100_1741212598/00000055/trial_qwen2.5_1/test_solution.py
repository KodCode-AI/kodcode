from solution import *

import pytest

def test_calculate_paths():
    assert calculate_paths(2) == 6
    assert calculate_paths(3) == 20
    assert calculate_paths(20) == 137846528820
    assert calculate_paths(1) == 2  # Only two possible paths for a 1x1 grid
    assert calculate_paths(0) == 1  # One path for a 0x0 grid, which is trivial

def test_calculate_paths_small_input():
    for i in range(1, 11):
        assert calculate_paths(i) == math.comb(2*i, i)

def test_calculate_paths_large_input():
    assert calculate_paths(100) == math.comb(200, 100)