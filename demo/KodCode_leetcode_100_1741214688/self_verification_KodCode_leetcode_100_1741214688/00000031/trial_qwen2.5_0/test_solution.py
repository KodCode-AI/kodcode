from solution import *

import pytest

def test_find_lexicographically_largest_palindrome():
    assert find_lexicographically_largest_palindrome("babad") == "bab"
    assert find_lexicographically_largest_palindrome("cbbd") == "bb"
    assert find_lexicographically_largest_palindrome("a") == "a"
    assert find_lexicographically_largest_palindrome("ac") == "a"
    assert find_lexicographically_largest_palindrome("racecar") == "racecar"
    assert find_lexicographically_largest_palindrome("banana") == "anana"
    assert find_lexicographically_largest_palindrome("abba") == "abba"
    assert find_lexicographically_largest_palindrome("abcde") == "e"

def test_edge_cases():
    assert find_lexicographically_largest_palindrome("") == ""
    assert find_lexicographically_largest_palindrome("a") == "a"
    assert find_lexicographically_largest_palindrome("aa") == "aa"
    assert find_lexicographically_largest_palindrome("aaa") == "aaa"