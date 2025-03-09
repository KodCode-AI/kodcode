from solution import *

def test_max_product_of_triplet():
    assert max_product_of_triplet([1, 2, 3]) == 6
    assert max_product_of_triplet([-1, -2, -3]) == -6
    assert max_product_of_triplet([-100, -200, 5, 1, 2]) == 20000
    assert max_product_of_triplet([-2, -3, 4, -5, -6, 1]) == 60
    assert max_product_of_triplet([1, -4, 3, -6, 7, 0]) == 168
    assert max_product_of_triplet([0, 2, 3, -5, 1, 4]) == 60
    assert max_product_of_triplet([10, -20, 2, -3, 4, -5, 5]) == 1000