from solution import *

import pytest
from solution import min_swaps_to_anagram

def test_min_swaps_to_anagram_equal_strings():
    assert min_swaps_to_anagram("abc", "abc") == 0

def test_min_swaps_to_anagram_swap_needed():
    assert min_swaps_to_anagram("abc", "bca") == 1

def test_min_swaps_to_anagram_multiple_swaps_needed():
    assert min_swaps_to_anagram("abcc", "ccba") == 2

def test_min_swaps_to_anagram_case_insensitivity():
    assert min_swaps_to_anagram("aBc", "Cba") == 3

def test_min_swaps_to_anagram_fail_length_mismatch():
    assert min_swaps_to_anagram("a", "ab") == -1

def test_min_swaps_to_anagram_empty_strings():
    assert min_swaps_to_anagram("", "") == 0

def test_min_swaps_to_anagram_multiple_characters():
    assert min_swaps_to_anagram("aabbcc", "ccbbaa") == 3