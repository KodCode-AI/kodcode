from solution import *

import pytest

def test_calculate_k():
    assert calculate_k(10, 6) == 5
    assert calculate_k(35, 15) == 58
    assert calculate_k(0, 5) == 25
    assert calculate_k(-10, -6) == 5
    assert calculate_k(1000000000, -1000000000) == 2000000000
    assert calculate_k(-1000000000, 1000000000) == 2000000000
    assert calculate_k(-1, -1) == 2

@pytest.mark.parametrize("m, n", [(-10, -6), (10, 6), (35, 15), (0, 5), (-1, -1)])
def test_calculate_k_positive(m, n):
    assert calculate_k(m, n) == calculate_k(abs(m), abs(n))

@pytest.mark.parametrize("m, n", [(10, -6), (-10, 6), (35, -15), (-35, 15), (-1, 1)])
def test_calculate_k_negative(m, n):
    assert calculate_k(m, n) == calculate_k(abs(m), abs(n))

@pytest.mark.parametrize("m, n", [(10, 0), (0, 10), (-10, 0), (0, -10)])
def test_calculate_k_zero(m, n):
    assert calculate_k(m, n) == m**2

@pytest.mark.parametrize("m, n", [(1000000000, 1000000000), (1000000000, -1000000000), (-1000000000, 1000000000)])
def test_calculate_k_large(m, n):
    assert calculate_k(m, n) == 2000000000