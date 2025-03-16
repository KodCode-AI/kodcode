from solution import *

from solution import merge_and_sum_dictionaries

def test_merge_and_sum_dictionaries_empty_dicts():
    assert merge_and_sum_dictionaries({}, {}) == {}

def test_merge_and_sum_dictionaries_no_overlap():
    assert merge_and_sum_dictionaries({'a': 1, 'b': 2}, {'c': 3, 'd': 4}) == {'a': 1, 'b': 2, 'c': 3, 'd': 4}

def test_merge_and_sum_dictionaries_overlap_same_value():
    assert merge_and_sum_dictionaries({'a': 1, 'b': 2}, {'a': 1, 'b': 2}) == {'a': 2, 'b': 4}

def test_merge_and_sum_dictionaries_overlap_different_values():
    assert merge_and_sum_dictionaries({'a': 1, 'b': 2}, {'a': 3, 'b': 4}) == {'a': 4, 'b': 6}

def test_merge_and_sum_dictionaries_within_a_single_dict():
    assert merge_and_sum_dictionaries({'a': 1, 'b': 2, 'c': 3}, {'b': 5, 'c': 7, 'd': 9}) == {'a': 1, 'b': 7, 'c': 10, 'd': 9}