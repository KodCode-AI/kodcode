from solution import *

from solution import all_subsets

def test_all_subsets_empty_set():
    assert all_subsets(set()) == [()]

def test_all_subsets_one_element():
    assert all_subsets({1}) == [(), (1,)]

def test_all_subsets_two_elements():
    assert all_subsets({1, 2}) == [(), (1,), (2,), (1, 2)]

def test_all_subsets_three_elements():
    assert all_subsets({1, 2, 3}) == [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]