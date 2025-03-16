from solution import *

import pytest

def test_calculate_paths():
    assert calculate_paths(2) == 6
    assert calculate_paths(3) == 20
    assert calculate_paths(1) == 2
    assert calculate_paths(20) == 137846528820

def test_calculate_paths_edge_cases():
    assert calculate_paths(0) == 1  # Edge case: 0x0 grid
    assert calculate_paths(1) == 2  # Edge case: 1x1 grid