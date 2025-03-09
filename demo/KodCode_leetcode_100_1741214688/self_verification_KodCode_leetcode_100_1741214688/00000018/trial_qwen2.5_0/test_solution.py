from solution import *

def test_min_cost_to_set():
    assert min_cost_to_set([1, 2, 3], [10, 15, 20]) == 10
    assert min_cost_to_set([2, 2, 2, 2, 2], [4, 2, 8, 1, 3]) == 5
    assert min_cost_to_set([1, 2, 3, 4, 5], [2, 4, 6, 8, 10]) == 30
    assert min_cost_to_set([5, 5, 5, 5], [1, 1, 1, 1]) == 4
    assert min_cost_to_set([10, 20, 30, 40, 50], [5, 3, 6, 8, 2]) == 5

def test_min_cost_to_set_with_zeros():
    assert min_cost_to_set([0, 0, 0, 0, 0], [1, 2, 3, 4, 5]) == 0