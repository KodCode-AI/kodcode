from solution import *

import pytest

def test_optimized_solution():
    assert optimized_solution(0) == 0
    assert optimized_solution(1) == 4
    assert optimized_solution(2) == 32
    assert optimized_solution(5) == 2000
    assert optimized_solution(10) == 120000

def test_edge_cases():
    assert optimized_solution(49) == 960400  # Based on the formula
    assert optimized_solution(50) == 1000000  # Based on the formula

def test_zero_limit():
    assert optimized_solution(0) == 0

def test_one_limit():
    assert optimized_solution(1) == 4