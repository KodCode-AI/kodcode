from solution import *

import pytest
from matrix_class import Matrix

def test_is_invertible():
    assert not Matrix(2, 2, 1, 2, 3, 4).is_invertible()
    assert Matrix(2, 2, 2, -1, -1, 2).is_invertible()
    assert not Matrix(2, 2, 1, 1, 1, 1).is_invertible()

def test_multiply_optimized():
    a = Matrix(2, 2, 1, 2, 3, 4)
    b = Matrix(2, 2, 2, 0, 1, 2)
    optimized = a.multiply_optimized(b)
    non_optimized = a * b
    assert (optimized.data == non_optimized.data).all()

def test_matrix_multiplication_dimensions():
    a = Matrix(2, 3, 1, 2, 3, 4, 5, 6)
    b = Matrix(3, 2, 7, 8, 9, 10, 11, 12)
    with pytest.raises(ValueError):
        a * b  # Dimension mismatch

def test_sherman_morrison():
    # Test case for sherman_morrison, assuming it is implemented with specific conditions
    # Placeholder implementation in the Matrix class raises NotImplementedError
    a = Matrix(2, 2, 1, 2, 3, 4)
    u = Matrix(2, 1, 1, 1)
    v = Matrix(2, 1, 1, 1)
    with pytest.raises(NotImplementedError):
        a.sherman_morrison(u, v)