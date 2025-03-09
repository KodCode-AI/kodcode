from solution import *

from solution import smallest_substring

def test_smallest_substring_single_char():
    assert smallest_substring("a") == "a"

def test_smallest_substring_short_string():
    assert smallest_substring("abc") == "a"

def test_smallest_substring_mixed_chars():
    assert smallest_substring("cbabc") == "abc"

def test_smallest_substring_empty_string():
    assert smallest_substring("") == ""

def test_smallest_substring_large_string():
    s = "zzzazzzzz"
    assert smallest_substring(s) == "a"

def test_smallest_substring_with_duplicates():
    s = "bacdbcd"
    assert smallest_substring(s) == "bcd"