from solution import *

import pytest

def test_max_product_of_triplet_positive_numbers():
    assert max_product_of_triplet([1, 2, 3]) == 6

def test_max_product_of_triplet_negative_numbers():
    assert max_product_of_triplet([-10, -10, 5, 2]) == 500

def test_max_product_of_triplet_mixed_numbers():
    assert max_product_of_triplet([-1, -2, -3, -4]) == -6

def test_max_product_of_triplet_with_zeross():
    assert max_product_of_triplet([-1, -1, 0, 2, 3]) == 6

def test_max_product_of_triplet_edge_cases():
    assert max_product_of_triplet([1, 2]) == 2
    assert max_product_of_triplet([1]) == 1
    assert max_product_of_triplet([-1]) == -1