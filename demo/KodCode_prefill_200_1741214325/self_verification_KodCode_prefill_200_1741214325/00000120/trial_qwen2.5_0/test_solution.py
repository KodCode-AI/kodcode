from solution import *

from solution import merge_and_sum_dicts

def test_merge_and_sum_dicts():
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 3, 'c': 4, 'd': 5}
    result = merge_and_sum_dicts(dict1, dict2)
    expected = {'a': 1, 'b': 5, 'c': 7, 'd': 5}
    assert result == expected

def test_merge_and_sum_dicts_with_same_key():
    dict1 = {'x': 10, 'y': 20}
    dict2 = {'x': 5, 'y': 30}
    result = merge_and_sum_dicts(dict1, dict2)
    expected = {'x': 15, 'y': 50}
    assert result == expected

def test_merge_and_sum_dicts_addition():
    dict1 = {'p': 100}
    dict2 = {'q': 200}
    result = merge_and_sum_dicts(dict1, dict2)
    expected = {'p': 100, 'q': 200}
    assert result == expected