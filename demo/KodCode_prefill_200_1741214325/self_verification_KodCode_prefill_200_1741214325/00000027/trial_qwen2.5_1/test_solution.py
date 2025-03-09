from solution import *

from solution import find_union

def test_find_union_with_unique_elements():
    assert find_union([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]

def test_find_union_with_common_elements():
    assert find_union([1, 2, 2, 3], [2, 3, 3, 4]) == [1, 2, 3, 4]

def test_find_union_with_mixed_data_types():
    assert find_union([1, 'a', 3], [2, 'a', 4]) == [1, 2, 3, 'a', 4]

def test_find_union_with_no_intersection():
    assert find_union([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]

def test_find_union_with_empty_lists():
    assert find_union([], []) == []
    assert find_union([], [1, 2, 3]) == [1, 2, 3]
    assert find_union([1, 2, 3], []) == [1, 2, 3]