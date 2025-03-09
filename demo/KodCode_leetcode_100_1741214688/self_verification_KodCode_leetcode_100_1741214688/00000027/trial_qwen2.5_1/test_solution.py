from solution import *

from solution import count_substring_occurrences

def test_count_substring_occurrences_positive():
    assert count_substring_occurrences(["abc", "trained", "mouse"], "train") == 1

def test_count_substring_occurrences_multiple_matches():
    assert count_substring_occurrences(["cat", "dog", "mousedog"], "dog") == 2

def test_count_substring_occurrences_no_matches():
    assert count_substring_occurrences(["hello", "world"], "universe") == 0

def test_count_substring_occurrences_single_word():
    assert count_substring_occurrences(["mouses"], "mouses") == 1

def test_count_substring_occurrences_empty_list():
    assert count_substring_occurrences([], "anything") == 0

def test_count_substring_occurrences_mixed_cases():
    assert count_substring_occurrences(["Trained", "mouse", "Cat"], "trained") == 1

def test_count_substring_occurrences_case_sensitive():
    assert count_substring_occurrences(["aBc", "ABCD", "Test"], "ab") == 1