from solution import *

from solution import filter_strings_by_substring

def test_filter_strings_by_substring_empty_list():
    assert filter_strings_by_substring([], "test") == []

def test_filter_strings_by_substring_no_match():
    assert filter_strings_by_substring(["hello", "world"], "test") == ["hello", "world"]

def test_filter_strings_by_substring_with_match():
    assert filter_strings_by_substring(["hello", "test", "world"], "test") == ["hello", "world"]

def test_filter_strings_by_substring_case_insensitive():
    assert filter_strings_by_substring(["HELLO", "test", "WORLD"], "Test") == ["HELLO", "WORLD"]

def test_filter_strings_by_substring_with_multiple_occurrences():
    assert filter_strings_by_substring(["apple", "banana", "cherry", "cantaloupe"], "a") == ["cherry"]