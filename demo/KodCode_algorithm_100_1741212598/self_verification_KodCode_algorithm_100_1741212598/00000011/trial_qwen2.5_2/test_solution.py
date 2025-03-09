from solution import *

``
import pytest

def test_square_root_approximate():
    a = 16
    initial_guess = 2.0
    max_iter = 1000
    tolerance = 1e-10
    
    root, iterations, converged = square_root_approximate(a, initial_guess, max_iter, tolerance)
    assert root == pytest.approx(4.0, abs=1e-10)
    assert iterations == 4
    assert converged

def test_square_root_approximate_zero():
    a = 0
    initial_guess = 2.0
    max_iter = 1000
    tolerance = 1e-10
    
    root, iterations, converged = square_root_approximate(a, initial_guess, max_iter, tolerance)
    assert root == 0.0
    assert iterations == 0
    assert converged

def test_square_root_approximate_negative_input():
    a = -1
    initial_guess = 2.0
    max_iter = 1000
    tolerance = 1e-10
    
    with pytest.raises(ValueError):
        square_root_approximate(a, initial_guess, max_iter, tolerance)

def test_square_root_approximate_tiny_tolerance():
    a = 16
    initial_guess = 2.0
    max_iter = 1000
    tolerance = 1e-20
    
    root, iterations, converged = square_root_approximate(a, initial_guess, max_iter, tolerance)
    assert root == pytest.approx(4.0, abs=1e-20)
    assert iterations >= 4
    assert converged

def test_square_root_approximate_max_iterations():
    a = 2
    initial_guess = 1.0
    max_iter = 5
    tolerance = 1e-10
    
    root, iterations, converged = square_root_approximate(a, initial_guess, max_iter, tolerance)
    assert root == pytest.approx(1.41421356237, abs=1e-10)
    assert iterations == 5
    assert not converged