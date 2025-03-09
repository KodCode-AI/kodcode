from solution import *

from solution import largest_string

def test_largest_string_single_sort():
    assert largest_string("1111111111222", 1) == "222111111111"

def test_largest_string_empty_string():
    assert largest_string("", 1) == ""

def test_largest_string_k_zero():
    assert largest_string("abc", 0) == "abc"

def test_largest_string_large_k():
    assert largest_string("1234", 2) == "4321"

def test_largest_string_with_repetitions():
    assert largest_string("zzzz", 2) == "zzzz"

def test_largest_string_mixed_activity():
    assert largest_string("aabcbbca", 2) == "aaabcbbca"

def test_largest_string_trivial_case():
    assert largest_string("a", 1) == "a"