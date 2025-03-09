from solution import *

def test_find_pythagorean_triplet_product():
    assert find_pythagorean_triplet_product(12) == 60
    assert find_pythagorean_triplet_product(1000) == 31875000
    assert find_pythagorean_triplet_product(30) == 2700
    assert find_pythagorean_triplet_product(100) == 61200
    assert find_pythagorean_triplet_product(200) == 1560000
    assert find_pythagorean_triplet_product(500) == 25500000
    assert find_pythagorean_triplet_product(789) == 38808900

test_find_pythagorean_triplet_product()