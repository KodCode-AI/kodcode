from solution import *

from solution import remove_duplicates

def test_remove_duplicates_empty_list():
    assert remove_duplicates([]) == []

def test_remove_duplicates_single_element():
    assert remove_duplicates([1]) == [1]

def test_remove_duplicates_with_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_with_duplicates_and_empty():
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5, 'a', 'a']) == [1, 2, 3, 4, 5, 'a']

def test_remove_duplicates_with_duplicates_and_strings():
    assert remove_duplicates(["apple", "banana", "apple", "orange"]) == ["apple", "banana", "orange"]