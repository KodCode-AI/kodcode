from solution import *

import pytest
from solution import min_swaps_to_anagram

def test_min_swaps_to_anagram():
    assert min_swaps_to_anagram("abc", "bca") == 1
    assert min_swaps_to_anagram("abcd", "dacb") == 3
    assert min_swaps_to_anagram("abcd", "dbca") == 2
    assert min_swaps_to_anagram("aaaa", "aaaa") == 0
    assert min_swaps_to_anagram("abc", "def") == -1  # s cannot be an anagram of t

def test_min_swaps_to_anagram_edge_cases():
    assert min_swaps_to_anagram("a", "a") == 0
    assert min_swaps_to_anagram("ab", "ba") == 1
    assert min_swaps_to_anagram("abc", "abc") == 0
    assert min_swaps_to_anagram("aabbcc", "aabbcc") == 0

def test_min_swaps_to_anagram_complex_cases():
    assert min_swaps_to_anagram("aabbcc", "cabbac") == 3
    assert min_swaps_to_anagram("analysis", "sitablyna") == 5
    assert min_swaps_to_anagram("standard", "tandstorm") == 4