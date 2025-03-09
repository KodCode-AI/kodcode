from solution import *

def test_count_substring_case_insensitive():
    assert count_substring("Hello World", "world") == 1
    assert count_substring("Python Programming", "pro") == 2
    assert count_substring("Case Insensitive", "INSENSITIVE") == 1
    assert count_substring("Repeated Repeated Repeated", "repeated") == 3

def test_count_substring_empty():
    assert count_substring("", "a") == 0
    assert count_substring("a", "") == 0

def test_count_substring_single_char():
    assert count_substring("aaa", "a") == 3
    assert count_substring("aaa", "b") == 0

def test_count_substring_overlapping():
    assert count_substring("ABCabcABCabc", "abc") == 2
    assert count_substring("ABCabcABCabc", "ABCA") == 1

def test_count_substring_no_occurrences():
    assert count_substring("No Substring Here", "notexistent") == 0