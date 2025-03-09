from solution import *

from solution import find_largest_palindrome

def test_find_largest_palindrome_single_char():
    assert find_largest_palindrome("a") == "a"

def test_find_largest_palindrome_even_length():
    assert find_largest_palindrome("abba") == "abba"

def test_find_largest_palindrome_odd_length():
    assert find_largest_palindrome("abbac") == "abbac"

def test_find_largest_palindrome_no_palindrome():
    assert find_largest_palindrome("random") == ""

def test_find_largest_palindrome_mixed_example():
    assert find_largest_palindrome("babad") == "bab"
    assert find_largest_palindrome("cbbd") == "bb"
    assert find_largest_palindrome("a") == "a"
    assert find_largest_palindrome("ac") == "c"