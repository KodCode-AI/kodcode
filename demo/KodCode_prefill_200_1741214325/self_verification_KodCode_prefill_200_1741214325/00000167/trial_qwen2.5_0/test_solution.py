from solution import *

from solution import count_missing_data

def test_count_missing_data_empty_list():
    assert count_missing_data([]) == 0

def test_count_missing_data_single_element():
    assert count_missing_data([1]) == 0

def test_count_missing_data_single_none():
    assert count_missing_data([None]) == 1

def test_count_missing_data_nested_none():
    assert count_missing_data([[None, 2], [3, None]]) == 2

def test_count_missing_data_complex_nested():
    assert count_missing_data([[None, 2, [None, 3]], [4, None, [5, None]]]) == 5

def test_count_missing_data_no_none():
    assert count_missing_data([[1, 2], [3, 4]]) == 0

def test_count_missing_data_mixed():
    assert count_missing_data([None, [1, None], [2, 3], None]) == 3