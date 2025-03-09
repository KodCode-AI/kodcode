from solution import *

from solution import longest_common_subsequence

def test_lcs_with_mask():
    assert longest_common_subsequence("abcde", "ace", "10111") == "ace"
    assert longest_common_subsequence("abcdef", "acdf", "010011") == "cdf"
    assert longest_common_subsequence("programming", "gaming", "0001001110") == "gmingm"
    assert longest_common_subsequence("abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyza", "1111111111111111111111100000") == "bcdefghijklmnopqrstuvwxyza"
    assert longest_common_subsequence("xyz", "xyz", "000") == "xyz"
    assert longest_common_subsequence("", "abc", "111") == ""
    assert longest_common_subsequence("abc", "", "000") == ""