from solution import *

import pytest

def test_calculate_paths_small_case():
    assert calculate_paths(2) == 6

def test_calculate_paths_large_case():
    assert calculate_paths(20) == 137846528820

def test_calculate_paths_edge_case():
    assert calculate_paths(1) == 2

def test_calculate_paths_zero_case():
    with pytest.raises(AssertionError):
        calculate_paths(0)  # Input should be positive, this should not be reached as per constraint

def test_calculate_paths_negative_case():
    with pytest.raises(AssertionError):
        calculate_paths(-5)  # Input should be positive