from solution import *

import pytest
import sys
import numpy as np

def test_matrix_operations():
    a = Matrix(2, 2)
    a[0, 0], a[0, 1], a[1, 0], a[1, 1] = 1, 2, 3, 4
    assert not a.is_invertible()

    b = Matrix(2, 2)
    b[0, 0], b[0, 1], b[1, 0], b[1, 1] = 2, -1, -1, 2
    assert b.is_invertible()
    assert isinstance(b.sherman_morrison(Matrix(2, 1, 1), Matrix(2, 1, 1)), Matrix)

    c = Matrix(2, 2)
    c[0, 0], c[0, 1], c[1, 0], c[1, 1] = 1, 1, 1, 1
    assert not c.is_invertible()

def test_matrix_multiplication():
    a = Matrix(2, 2, 1, 2, 3, 4)
    b = Matrix(2, 2, 1, 1, 2, 2)
    c = a * b
    expected_result = np.array([[5, 7], [11, 15]])
    np.testing.assert_array_equal(c._matrix, expected_result)

def test_matrix_dimensions():
    a = Matrix(2, 2, 1, 2, 3, 4)
    with pytest.raises(ValueError):
        a * b.T

def test_multiply_optimized():
    a = Matrix(2, 2, 1, 2, 3, 4)
    b = Matrix(2, 2, 1, 1, 2, 2)
    optimized_result = a.multiply_optimized(b)
    expected_result = np.dot(a._matrix, b._matrix)
    np.testing.assert_array_equal(optimized_result._matrix, expected_result)

def test_exception_on_invertible():
    a = Matrix(2, 2, 1, 1, 1, 1)
    with pytest.raises(np.linalg.LinAlgError):
        a.inv()

def test_is_invertible():
    a = Matrix(2, 2, 1, 2, 3, 4)
    assert not a.is_invertible()
    b = Matrix(2, 2, 1, 2, -1, 2)
    assert b.is_invertible()