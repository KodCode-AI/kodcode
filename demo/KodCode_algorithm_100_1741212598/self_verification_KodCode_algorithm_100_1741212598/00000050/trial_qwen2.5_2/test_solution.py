from solution import *

import pytest
from solution import Matrix

def test_matrix_init():
    a = Matrix(2, 2)
    a[0, 0], a[0, 1], a[1, 0], a[1, 1] = 1, 2, 3, 4
    assert a.shape() == (2, 2)

def test_matrix_get_set_item():
    a = Matrix([[1, 2], [3, 4]])
    assert a[0, 0] == 1
    a[0, 0] = 5
    assert a[0, 0] == 5

def testnegative_matrix():
    a = -Matrix([[1, 2], [3, 4]])
    assert a[0, 0] == -1
    assert a[0, 1] == -2

def test_matrix_multiplication():
    a = Matrix(2, 2)
    a[0, 0], a[0, 1], a[1, 0], a[1, 1] = 1, 2, 3, 4
    b = Matrix(2, 2)
    b[0, 0], b[0, 1], b[1, 0], b[1, 1] = 5, 6, 7, 8
    c = a * b
    assert c[0, 0] == 19
    assert c[0, 1] == 22
    assert c[1, 0] == 43
    assert c[1, 1] == 50

def test_matrix_is_invertible():
    a = Matrix([[1, 2], [3, 4]])
    assert not a.is_invertible()
    b = Matrix([[2, -1], [-1, 2]])
    assert b.is_invertible()

def test_matrix_sherman_morrison():
    a = Matrix([[2, -1], [-1, 2]])
    u = Matrix(2, 1, [1, 1])
    v = Matrix(2, 1, [1, 1])
    result = a.sherman_morrison(u, v)
    assert result[0, 0] == 1.5
    assert result[0, 1] == -0.5
    assert result[1, 0] == -0.5
    assert result[1, 1] == 1.5

def test_matrix_multiply_optimized():
    a = Matrix(2, 3)
    a[0, 0], a[0, 1], a[0, 2], a[1, 0], a[1, 1], a[1, 2] = 1, 2, 3, 4, 5, 6
    b = Matrix(3, 2)
    b[0, 0], b[0, 1], b[1, 0], b[1, 1], b[2, 0], b[2, 1] = 7, 8, 9, 10, 11, 12
    c = a.multiply_optimized(b)
    assert c[0, 0] == 58
    assert c[0, 1] == 64
    assert c[1, 0] == 139
    assert c[1, 1] == 154

def test_matrix_non_matching_shapes():
    a = Matrix(2, 2)
    b = Matrix(2, 3)
    with pytest.raises(ValueError):
        _ = a * b