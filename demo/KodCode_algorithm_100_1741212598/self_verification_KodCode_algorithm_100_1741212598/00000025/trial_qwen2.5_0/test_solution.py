from solution import *

`python
import pytest

def test_fibonacci_iterative():
    assert fibonacci_iterative(0) == 0
    assert fibonacci_iterative(1) == 1
    assert fibonacci_iterative(10) == 55
    with pytest.raises(ValueError):
        fibonacci_iterative(-1)

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

def test_fibonacci_matrix():
    assert fibonacci_matrix(0) == 0
    assert fibonacci_matrix(1) == 1
    assert fibonacci_matrix(10) == 55
    with pytest.raises(ValueError):
        fibonacci_matrix(-1)

def test_fibonacci_consistency():
    for n in range(20):
        assert fibonacci_iterative(n) == fibonacci_memoization(n) == fibonacci_binet(n) == fibonacci_matrix(n)