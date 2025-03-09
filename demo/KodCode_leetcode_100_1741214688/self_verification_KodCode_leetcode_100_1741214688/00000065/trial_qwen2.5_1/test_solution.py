from solution import *

def test_find_missing_element():
    assert find_missing_element([1, 2, 4, 5, 6]) == 3
    assert find_missing_element([1, 3, 4, 5]) == 2
    assert find_missing_element([1, 2, 3, 5]) == 4
    assert find_missing_element([2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert find_missing_element([1, 2, 3, 4, 5, 7, 8, 9, 10]) == 6

def test_edge_cases():
    assert find_missing_element([1]) == 2
    assert find_missing_element([2]) == 1
    assert find_missing_element([3, 4, 5]) == 2