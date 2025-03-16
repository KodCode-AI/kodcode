from solution import *

from solution import find_common_elements

def test_find_common_elements():
    assert find_common_elements([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]

def test_find_common_elements_with_no_common():
    assert find_common_elements([1, 2, 3], [4, 5, 6]) == []

def test_find_common_elements_with_duplicates():
    assert find_common_elements([1, 2, 2, 3], [2, 2, 3, 4]) == [2, 3]

def test_find_common_elements_with_empty_lists():
    assert find_common_elements([], [1, 2, 3]) == []
    assert find_common_elements([1, 2, 3], []) == []