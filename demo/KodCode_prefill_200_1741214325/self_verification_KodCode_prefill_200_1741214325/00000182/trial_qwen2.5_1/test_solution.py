from solution import *

from solution import find_subsets

def test_find_subsets_empty():
    assert find_subsets([]) == [[]]

def test_find_subsets_one_element():
    assert find_subsets([1]) == [[], [1]]

def test_find_subsets_two_elements():
    assert find_subsets([1, 2]) == [[], [1], [2], [1, 2]]

def test_find_subsets_three_elements():
    assert find_subsets([1, 2, 3]) == [
        [], 
        [1], 
        [2], 
        [1, 2], 
        [3], 
        [1, 3], 
        [2, 3], 
        [1, 2, 3]
    ]