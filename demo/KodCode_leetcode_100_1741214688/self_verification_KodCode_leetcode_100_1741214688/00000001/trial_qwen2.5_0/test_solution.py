from solution import *

from solution import largest_string

def test_largest_string_no_operations():
    assert largest_string("abc", 0) == "abc"

def test_largest_string_k_equal_to_string_length():
    assert largest_string("abc", 3) == "cba"

def test_largest_string_k_half_string_length():
    assert largest_string("abc", 1) == "cba"

def test_largest_string_k_greater_than_string_length_half():
    assert largest_string("abc", 2) == "cba"

def test_largest_string_with_operations():
    assert largest_string("edcba", 3) == "eabcd"

def test_largest_string_with_operations_empty_string():
    assert largest_string("", 2) == ""

def test_largest_string_with_operations_initially_sorted_string():
    assert largest_string("abcdef", 2) == "abcdef"

def test_largest_string_with_operations_complex_string():
    assert largest_string("acbzae", 2) == "aeabcz"

def test_largest_string_with_operations_complex_string_after_first_operation():
    assert largest_string("aeabcz", 1) == "aceabz"