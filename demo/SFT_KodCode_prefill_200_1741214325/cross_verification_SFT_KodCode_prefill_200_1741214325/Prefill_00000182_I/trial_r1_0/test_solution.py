from solution import *

from solution import find_subsets

def test_find_subsets_empty_set():
    assert find_subsets(set()) == [[]]

def test_find_subsets_one_element():
    assert find_subsets({1}) == [[], [1]]

def test_find_subsets_two_elements():
    assert find_subsets({1, 2}) == [[], [1], [2], [1, 2]]

def test_find_subsets_three_elements():
    assert find_subsets({1, 2, 3}) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

def test_find_subsets_four_elements():
    s = {1, 2, 3, 4}
    subsets = find_subsets(s)
    assert len(subsets) == 16  # 2^n where n is the number of elements in the set
    assert set(map(tuple, subsets)) == set(map(tuple, [
        [], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3],
        [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]
    ]))