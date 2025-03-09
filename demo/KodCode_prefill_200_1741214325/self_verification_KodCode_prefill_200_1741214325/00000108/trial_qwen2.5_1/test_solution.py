from solution import *

from solution import count_substring_occurrences

def test_count_substring_occurrences_empty():
    assert count_substring_occurrences("", "a") == 0

def test_count_substring_occurrences_single():
    assert count_substring_occurrences("aaa", "a") == 3
    assert count_substring_occurrences("aaa", "aa") == 1

def test_count_substring_occurrences_multiple():
    assert count_substring_occurrences("abababab", "ab") == 4
    assert count_substring_occurrences("mississippi", "iss") == 2

def test_count_substring_occurrences_overlap():
    assert count_substring_occurrences("banana", "ana") == 1
    assert count_substring_occurrences("pineapple", "apple") == 1
    assert count_substring_occurrences("hellohellohello", "hello") == 3

def test_count_substring_occurrences_not_found():
    assert count_substring_occurrences("hello", "world") == 0
    assert count_substring_occurrences("abcd", "ef") == 0

def test_count_substring_occurrences_with_case_insensitive():
    assert count_substring_occurrences("HelloWorld", "oW") == 0
    assert count_substring_occurrences("HelloWorld", "oW", case_sensitive=False) == 1