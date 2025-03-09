from solution import *

import pytest

def test_optimized_integer_square_root():
    assert optimized_integer_square_root(15) == 3
    assert optimized_integer_square_root(31) == 5
    assert optimized_integer_square_root(25) == 5
    assert optimized_integer_square_root(1) == 1
    assert optimized_integer_square_root(0) == 0
    assert optimized_integer_square_root(2_147_483_647) == 46340
    with pytest.raises(ValueError):
        optimized_integer_square_root(-1)

# Additional corner and edge case tests
def test_perfect_squares_1():
    assert optimized_integer_square_root(16) == 4

def test_perfect_squares_2():
    assert optimized_integer_square_root(81) == 9

def test_large_number():
    assert optimized_integer_square_root(1_000_000_000) == 31622

def test_zero():
    assert optimized_integer_square_root(0) == 0

def test_one():
    assert optimized_integer_square_root(1) == 1

def test_single_digit_numbers():
    for i in range(1, 10):
        assert optimized_integer_square_root(i) == int(i ** 0.5)

def test_edge_between_perfect_squares():
    for i in range(10, 20):
        assert optimized_integer_square_root(i*i-1) == (i-1)
        assert optimized_integer_square_root(i*i) == i

def test_big_number():
    assert optimized_integer_square_root(2147483647) == 46340