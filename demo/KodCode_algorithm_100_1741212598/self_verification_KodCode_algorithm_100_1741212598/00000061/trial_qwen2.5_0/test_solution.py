from solution import *

``
import pytest

def test_find_pythagorean_triplet_product():
    assert find_pythagorean_triplet_product(12) == 60
    assert find_pythagorean_triplet_product(1000) == 31875000
    assert find_pythagorean_triplet_product(30) == 2700
    assert find_pythagorean_triplet_product(100) == 918000
    assert find_pythagorean_triplet_product(999) == 31863500  # Test upper bound
    assert find_pythagorean_triplet_product(3) == -1  # No solution for N = 3

test_find_pythagorean_triplet_product()