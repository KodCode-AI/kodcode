from solution import *

import pytest

def test_find_largest_palindromic_substring():
    assert find_largest_palindromic_substring("babad") == "bab" or find_largest_palindromic_substring("babad") == "aba"
    assert find_largest_palindromic_substring("cbbd") == "bb"
    assert find_largest_palindromic_substring("a") == "a"
    assert find_largest_palindromic_substring("ac") == "a" or find_largest_palindromic_substring("ac") == "c"
    assert find_largest_palindromic_substring("racecar") == "racecar"
    assert find_largest_palindromic_substring("banana") == "anana" or find_largest_palindromic_substring("banana") == "anana"