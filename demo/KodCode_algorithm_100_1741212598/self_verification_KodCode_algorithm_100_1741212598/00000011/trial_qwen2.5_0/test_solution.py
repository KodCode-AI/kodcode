from solution import *

from solution import square_root_approximate

def test_square_root_approximate_positive_numbers():
    a = 16
    initial_guess = 2.0
    max_iter = 1000
    tolerance = 1e-10
    root, iterations, converged = square_root_approximate(a, initial_guess, max_iter, tolerance)
    assert root == 4.0
    assert iterations <= max_iter
    assert converged

def test_square_root_approximate_negative_numbers():
    a = -16
    initial_guess = 2.0
    max_iter = 1000
    tolerance = 1e-10
    with pytest.raises(ValueError):
        square_root_approximate(a, initial_guess, max_iter, tolerance)

def test_square_root_approximate_single_iteration():
    a = 16
    initial_guess = 2.0
    max_iter = 1  # Force a single iteration
    tolerance = 1e-10
    root, iterations, converged = square_root_approximate(a, initial_guess, max_iter, tolerance)
    assert root != 4.0
    assert iterations == max_iter
    assert not converged

def test_square_root_approximate_with_zero():
    a = 0
    initial_guess = 2.0
    max_iter = 1000
    tolerance = 1e-10
    root, iterations, converged = square_root_approximate(a, initial_guess, max_iter, tolerance)
    assert root == 0.0
    assert iterations <= max_iter
    assert converged

def test_square_root_approximate_high_tolerance():
    a = 16
    initial_guess = 2.0
    max_iter = 9999
    tolerance = 1.0  # High tolerance to force multiple iterations
    root, iterations, converged = square_root_approximate(a, initial_guess, max_iter, tolerance)
    assert root == 4.0
    assert iterations <= max_iter
    assert converged