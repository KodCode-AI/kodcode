from solution import *

from solution import merge_dictionaries

def test_merge_dictionaries_same_key():
    assert merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) == {'a': 1, 'b': 5, 'c': 4}

def test_merge_dictionaries_no_overlap():
    assert merge_dictionaries({'a': 1, 'b': 2}, {'c': 3, 'd': 4}) == {'a': 1, 'b': 2, 'c': 3, 'd': 4}

def test_merge_dictionaries_with_zeros():
    assert merge_dictionaries({'x': 0, 'y': 0}, {'y': 1, 'z': 2}) == {'x': 0, 'y': 1, 'z': 2}

def test_merge_dictionaries_negative_values():
    assert merge_dictionaries({'a': -2, 'b': -3}, {'b': -1, 'c': -5}) == {'a': -2, 'b': -4, 'c': -5}