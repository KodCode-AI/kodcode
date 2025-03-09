from solution import *

from solution import filter_strings

def test_filter_strings_empty_list():
    assert filter_strings([], "test") == []

def test_filter_strings_no_matches():
    assert filter_strings(["apple", "banana", "cherry"], "date") == []

def test_filter_strings_with_matches_at_beginning():
    assert filter_strings(["apple", "date", "cherry"], "a") == ["apple", "date"]

def test_filter_strings_with_matches_at_end():
    assert filter_strings(["apple", "date", "cherry"], "ry") == ["cherry"]

def test_filter_strings_with_matches_in_middle():
    assert filter_strings(["apple", "banana", "cherry"], "na") == ["banana"]

def test_filter_strings_with_substring_case_insensitive():
    assert filter_strings(["Apple", "Banana", "cherry"], "a") == ["Apple", "Banana"]