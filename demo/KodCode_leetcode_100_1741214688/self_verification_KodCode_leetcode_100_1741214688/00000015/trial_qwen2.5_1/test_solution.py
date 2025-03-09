from solution import *

def test_longest_common_subsequence_with_mask():
    assert longest_common_subsequence_with_mask("abcde", "ace", "01010") == "ace"
    assert longest_common_subsequence_with_mask("abc", "abc", "000") == "abc"
    assert longest_common_subsequence_with_mask("abc", "def", "11") == "bc"
    assert longest_common_subsequence_with_mask("abcd", "ace", "0001") == "d"

def test_longest_common_subsequence_with_mask_empty_mask():
    assert longest_common_subsequence_with_mask("abc", "abc", "") == "abc"