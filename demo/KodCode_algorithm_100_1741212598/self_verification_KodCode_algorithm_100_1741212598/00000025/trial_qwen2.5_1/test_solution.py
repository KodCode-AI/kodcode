from solution import *

import pytest

def test_fibonacci_iterative():
    assert fibonacci_iterative(0) == 0
    assert fibonacci_iterative(1) == 1
    assert fibonacci_iterative(10) == 55
    with pytest.raises(ValueError):
        fibonacci_iterative(-1)

def test_fibonacci_recursive():
    assert fibonacci_recursive(0) == 0
    assert fibonacci_recursive(1) == 1
    assert fibonacci_recursive(10) == 55
    with pytest.raises(ValueError):
        fibonacci_recursive(-1)

def test_fibonacci_memoization():
    assert fibonacci_memoization(0) == 0
    assert fibonacci_memoization(1) == 1
    assert fibonacci_memoization(10) == 55
    with pytest.raises(ValueError):
        fibonacci_memoization(-1)

def test_fibonacci_binet():
    assert fibonacci_binet(0) == 0
    assert fibonacci_binet(1) == 1
    assert fibonacci_binet(10) == 55
    with pytest.raises(ValueError):
        fibonacci_binet(-1)

def test_fibonacci_matrix_exponentiation():
    assert fibonacci_matrix_exponentiation(0) == 0
    assert fibonacci_matrix_exponentiation(1) == 1
    assert fibonacci_matrix_exponentiation(10) == 55
    with pytest.raises(ValueError):
        fibonacci_matrix_exponentiation(-1)

def test_fibonacci_precision():
    assert fibonacci_binet(100) == 354224848179261915075
    assert fibonacci_matrix_exponentiation(100) == 354224848179261915075

def test_matrix_multiply():
    A = [[1, 2], [3, 4]]
    B = [[2, 0], [1, 2]]
    expected = [[4, 4], [10, 8]]
    assert matrix_multiply(A, B) == expected