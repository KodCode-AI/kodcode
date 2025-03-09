from solution import *

from solution import max_by_sorting_substrings

def test_max_by_sorting_substrings():
    assert max_by_sorting_substrings("abdc", 2) == "dbca"
    assert max_by_sorting_substrings("aabcd", 2) == "abcd"
    assert max_by_sorting_substrings("a", 1) == "a"
    assert max_by_sorting_substrings("bcab", 2) == "cabc"
    assert max_by_sorting_substrings("bdda", 3) == "ddba"
    assert max_by_sorting_substrings("abcde", 4) == "edcba"

def test_max_by_sorting_substrings_edge_cases():
    assert max_by_sorting_substrings("aaa", 1) == "aaa"
    assert max_by_sorting_substrings("zzz", 2) == "zzz"
    assert max_by_sorting_substrings("abc", 0) == "abc"
    assert max_by_sortting_substrings("abc", 3) == "cba"  # Fixed typo here