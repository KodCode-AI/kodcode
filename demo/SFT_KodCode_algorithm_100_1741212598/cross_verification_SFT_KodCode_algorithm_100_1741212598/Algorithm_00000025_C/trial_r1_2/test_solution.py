from solution import *

import pytest
from solution import (
    fibonacci_iterative, 
    fibonacci_recursive, 
    fibonacci_binets, 
    fibonacci_matrix
)

def test_fibonacci_iterative():
    assert fibonacci_iterative(0) == 0
    assert fibonacci_iterative(1) == 1
    assert fibonacci_iterative(2) == 1
    assert fibonacci_iterative(10) == 55
    assert fibonacci_iterative(20) == 6765

def test_fibonacci_recursive():
    assert fibonacci_recursive(0) == 0
    assert fibonacci_recursive(1) == 1
    assert fibonacci_recursive(2) == 1
    assert fibonacci_recursive(10) == 55
    assert fibonacci_recursive(20) == 6765

def test_fibonacci_binets():
    assert fibonacci_binets(0) == 0
    assert fibonacci_binets(1) == 1
    assert fibonacci_binets(2) == 1
    assert fibonacci_binets(10) == 55
    assert fibonacci_binets(20) == 6765

def test_fibonacci_matrix():
    assert fibonacci_matrix(0) == 0
    assert fibonacci_matrix(1) == 1
    assert fibonacci_matrix(2) == 1
    assert fibonacci_matrix(10) == 55
    assert fibonacci_matrix(20) == 6765

def test_large_input_fibonacci_matrix():
    assert fibonacci_matrix(50) == 12586269025

def test_negative_input():
    with pytest.raises(ValueError):
        fibonacci_iterative(-1)
    with pytest.raises(ValueError):
        fibonacci_recursive(-1)
    with pytest.raises(ValueError):
        fibonacci_binets(-1)
    with pytest.raises(ValueError):
        fibonacci_matrix(-1)