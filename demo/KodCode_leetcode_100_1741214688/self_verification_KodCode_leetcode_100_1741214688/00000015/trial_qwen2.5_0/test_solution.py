from solution import *

from solution import longest_common_subsequence

def test_lcs_with_mask():
    assert longest_common_subsequence("abcde", "ace", "10101") == "ace"
    assert longest_common_subsequence("abcdeg", "aceg", "010101") == "aceg"
    assert longest_common_subsequence("abcd", "abcd", "1111") == "abcd"
    assert longest_common_subsequence("abc", "def", "001") == "c"
    assert longest_common_subsequence("abcde", "ace", "00101") == ""

def test_lcs_without_mask():
    assert longest_common_subsequence("abcde", "ace", "00000") == ""
    assert longest_common_subsequence("abcde", "ace", "11111") == "ace"