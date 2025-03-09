from solution import *

def test_min_cost():
    assert min_cost([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) == 10  # Setting all to 1 has the minimum cost

def test_min_cost_with_zeros():
    assert min_cost([0, 0, 0, 0], [1, 2, 3, 4]) == 0  # No cost since nums are already zeroes

def test_min_cost_all_same():
    assert min_cost([5, 5, 5, 5], [1, 2, 3, 4]) == 4  # Setting 5 to 0 with the least cost

def test_min_cost_mixed_values():
    assert min_cost([2, 5, 3, 7, 1], [4, 5, 2, 3, 1]) == 5  # Setting 1 to 0 has the least cost

def test_min_cost_single_element():
    assert min_cost([1], [10]) == 10  # Only one element, setting it to 0 incurs the full cost