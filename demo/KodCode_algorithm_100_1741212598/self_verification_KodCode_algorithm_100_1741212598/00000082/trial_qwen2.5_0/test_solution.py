from solution import *

import pytest

def test_lcs_positive():
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == (4, ["GTAB", "GBAB"])
    assert longest_common_subsequence("ABCBDAB", "BDCAB") == (4, ["BCAB", "BDAB"])

def test_lcs_single_char():
    assert longest_common_subsequence("a", "a") == (1, ["a"])
    assert longest_common_subsequence("a", "b") == (0, [])

def test_lcs_empty_string():
    assert longest_common_subsequence("", "a") == (0, [])
    assert longest_common_subsequence("a", "") == (0, [])

def test_lcs_all_different():
    assert longest_common_subsequence("abc", "def") == (0, [])

def test_lcs_common_chars():
    assert longest_common_subsequence("hello", "world") == (2, ["lo"])
    assert longest_common_subsequence("helloworld", "world") == (5, ["world"])