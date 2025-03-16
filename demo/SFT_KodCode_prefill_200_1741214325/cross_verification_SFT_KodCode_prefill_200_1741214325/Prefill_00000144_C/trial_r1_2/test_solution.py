from solution import *

import pytest
from solution import max_triplet_product

def test_max_triplet_product_with_positive_numbers():
    assert max_triplet_product([1, 2, 3]) == 6

def test_max_triplet_product_with_mixed_numbers():
    assert max_triplet_product([1, 10, -5, 1, -100]) == 5000  # -5 * -100 * 10

def test_max_triplet_product_with_negative_numbers():
    assert max_triplet_product([-1, -2, -3, -4]) == -6

def test_max_triplet_product_with_zero():
    assert max_triplet_product([0, 0, 0]) == 0

def test_max_triplet_product_with_small_array():
    with pytest.raises(ValueError):
        max_triplet_product([1, 2])

def test_max_triplet_product_with_larger_numbers():
    assert max_triplet_product([0, -2, -8, -7, 0]) == 0  # 0 * 0 * -7
    assert max_triplet_product([-5, -4, 2, 2]) == 40  # -5 * -4 * 2