from solution import *

def test_find_closest_element():
    assert find_closest_element([2, 1, 3, 4, 0], 1) == 1
    assert find_closest_element([10, 2, 1, 20, 30, 40], 21) == 3
    assert find_closest_element([7, 8, 9, 5, 6, 4, 3, 2, 1], 5) == 3
    assert find_closest_element([1, 3, 5, 7, 9, 11], 6) == 3
    assert find_closest_element([1, 3, 2], 2) == 2
    assert find_closest_element([0, 1, 2, 6, 5, 4], 3) == 2