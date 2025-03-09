from solution import *

def test_longest_substring_with_all_chars():
    assert longest_substring_with_all_chars("aabbcc") == "aabbcc"
    assert longest_substring_with_all_chars("abcabcbb") == "abc"
    assert longest_substring_with_all_chars("abba") == "ab"
    assert longest_substring_with_all_chars("dvdf") == "vdf"
    assert longest_substring_with_all_chars("") == ""
    assert longest_substring_with_all_chars("x") == ""
    assert longest_substring_with_all_chars("xyy") == "xy"