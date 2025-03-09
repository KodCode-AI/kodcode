from solution import *

``
from solution import find_pythagorean_triplet_product

def test_find_pythagorean_triplet_product():
    assert find_pythagorean_triplet_product(12) == 60
    assert find_pythagorean_triplet_product(30) == 2700
    assert find_pythagorean_triplet_product(1000) == 31875000
    assert find_pythagorean_triplet_product(3) == 0  # No valid triplet for N < 12
    assert find_pythagorean_triplet_product(20) == 1200

test_find_pythagorean_triplet_product()