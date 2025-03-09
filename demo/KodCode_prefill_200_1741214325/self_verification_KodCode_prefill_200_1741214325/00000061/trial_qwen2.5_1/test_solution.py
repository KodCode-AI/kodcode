from solution import *

from solution import find_unique_element

def test_find_unique_element():
    assert find_unique_element([2, 3, 4, 5, 4]) == 1
    assert find_unique_element([1, 2, 3, 4, 4, 3, 2]) == 0
    assert find_unique_element([1, 1, 2, 2, 3, 3]) == -1
    assert find_unique_element([10, 20, 20, 30]) == 0
    assert find_unique_element([7, 7, 7, 7]) == -1