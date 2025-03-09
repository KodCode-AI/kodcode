from solution import *

from solution import max_product

def test_max_product():
    assert max_product([10, 20, 30, 40], [5, 25, 30, 15], 2) == 266
    assert max_product([7, 3, 1], [1, 2, 3], 2) == 12
    assert max_product([4, 2, 4, 5, 6], [2, 1, 3, 3, 5], 3) == 18
    assert max_product([1, 2, 3], [2, 1, 3], 3) == 3
    assert max_product([10, 10], [5, 5], 2) == 0

def test_dp_cache():
    assert max_product([5, 6, 2, 7], [2, 1, 6, 10], 3) == 48