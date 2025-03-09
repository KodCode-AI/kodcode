from solution import *

import pytest

def test_liouville_lambda_single_int():
    assert liouville_lambda(10) == 1
    assert liouville_lambda(7) == -1
    assert liouville_lambda(1) == 1

def test_liouville_lambda_list_of_ints():
    assert liouville_lambda([10, 11, 12]) == [1, -1, -1]
    assert liouville_lambda([100, 97, 98]) == [1, -1, -1]

def test_liouville_lambda_edge_cases():
    assert liouville_lambda(0) == 1  # By convention, L(0) = 1
    assert liouville_lambda([-10]) == 1 # Negative numbers are not considered in this implementation
    assert liouville_lambda([]) == []  # Empty list should return an empty list
    assert liouville_lambda([1000000, 999999]) == [1, -1]  # Large numbers

def test_input_type():
    with pytest.raises(TypeError):
        liouville_lambda("10")  # String input
    with pytest.raises(TypeError):
        liouville_lambda([1, "2"])  # List with a string

def test_prime_factors():
    factors = prime_factors(60)
    assert len(factors) == 4
    assert set(factors) == {2, 3, 5}