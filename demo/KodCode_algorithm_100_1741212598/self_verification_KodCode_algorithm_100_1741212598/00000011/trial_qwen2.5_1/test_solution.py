from solution import *

``
import pytest

def test_square_root_approximate_positive():
    a = 16
    root, iterations, converged = square_root_approximate(a)
    assert abs(root - 4.0) < 1e-14
    assert iterations <= 9999
    assert converged

def test_square_root_approximate_zero():
    a = 0
    root, iterations, converged = square_root_approximate(a)
    assert root == 0
    assert iterations <= 9999
    assert converged

def test_square_root_approximate_one():
    a = 1
    root, iterations, converged = square_root_approximate(a)
    assert abs(root - 1.0) < 1e-14
    assert iterations <= 9999
    assert converged

def test_square_root_approximate_negative():
    a = -1
    with pytest.raises(ValueError):
        square_root_approximate(a)

def test_square_root_approximate_decimal():
    a = 25.0
    root, iterations, converged = square_root_approximate(a, initial_guess=2.5)
    assert abs(root - 5.0) < 1e-14
    assert iterations <= 9999
    assert converged

def test_square_root_approximate_complex_initial_guess():
    a = 25.0
    root, iterations, converged = square_root_approximate(a, initial_guess=3.0)
    assert abs(root - 5.0) < 1e-14
    assert iterations <= 9999
    assert converged