from solution import *

import pytest

def test_make_smallest_palindrome():
    assert make_smallest_palindrome("egcfe", 2) == "efcfe"
    assert make_smallest_palindrome("abcd", 1) == ""
    assert make_smallest_palindrome("seven", 2) == "evens"
    assert make_smallest_palindrome("aabb", 2) == "abba"
    assert make_smallest_palindrome("abcde", 1) == ""
    assert make_smallest_palindrome("abcde", 2) == "abced"
    assert make_smallest_palindrome("abcde", 4) == "abcde"
    assert make_smallest_palindrome("abcdefg", 5) == "abcddfa"

def test_make_smallest_palindrome_with_limit():
    assert make_smallest_palindrome("abcd", 3) == "abdc"  # only 3 swaps, not enough to make abcd

def test_make_smallest_palindrome_large_number_of_swaps():
    assert make_smallest_palindrome("abbba", 3) == "abbbb"  # swaps to make it a palindrome

def test_make_smallest_palindrome_return_empty_string_if_impossible():
    assert make_smallest_palindrome("abcd", 2) == ""  # only 2 swaps, not enough

pytest.main(['-v', 'tests.py'])