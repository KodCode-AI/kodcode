from solution import *

from solution import binomial_coefficient

def test_binomial_coefficient_small_values():
    assert binomial_coefficient(5, 2) == 10
    assert binomial_coefficient(6, 3) == 20

def test_binomial_coefficient_large_values():
    assert binomial_coefficient(20, 10) == 184756
    assert binomial_coefficient(25, 15) == 3268760

def test_binomial_coefficient_edge_cases():
    assert binomial_coefficient(0, 0) == 1
    assert binomial_coefficient(1, 0) == 1
    assert binomial_coefficient(1, 1) == 1

def test_binomial_coefficient_mixed_sign_numbers():
    # n and k should be non-negative integers
    assert binomial_coefficient(5, -1) is None
    assert binomial_coefficient(-5, 2) is None
    assert binomial_coefficient(5, 6) == 0  # n < k, which is not allowed