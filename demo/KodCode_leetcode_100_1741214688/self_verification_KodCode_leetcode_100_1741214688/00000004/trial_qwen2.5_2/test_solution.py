from solution import *

def test_count_balanced_substrings():
    assert count_balanced_substrings("abcabc", 2) == 3
    assert count_balanced_substrings("aaabbbccc", 3) == 1
    assert count_balanced_substrings("aabac", 2) == 3
    assert count_balanced_substrings("aabbcc", 3) == 6
    assert count_balanced_substrings("xyz", 3) == 1
    assert count_balanced_substrings("xyzz", 4) == 1