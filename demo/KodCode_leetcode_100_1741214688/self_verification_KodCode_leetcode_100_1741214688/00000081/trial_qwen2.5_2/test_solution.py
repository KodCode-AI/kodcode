from solution import *

def test_longest_substring_with_all_chars():
    assert longest_substring_with_all_chars("xyyzyzyx") == "zyz"
    assert longest_substring_with_all_chars("a") == ""
    assert longest_substring_with_all_chars("abcabcbb") == "abc"
    assert longest_substring_with_all_chars("abacdefabacdef") == "abacdef"
    assert longest_substring_with_all_chars("aaabbcbbbab") == "bbcb"

def test_longest_substring_with_empty_string():
    assert longest_substring_with_all_chars("") == ""

def test_longest_substring_with_multiple_substrings():
    assert longest_substring_with_all_chars("bbaacdbabb") == "acdbab"
    assert longest_substring_with_all_chars("aaacccbbb") == "acccb"

def test_longest_substring_with_repeated_characters():
    assert longest_substring_with_all_chars("zzabzz") == "zab"

def test_longest_substring_with_same_characters():
    assert longest_substring_with_all_chars("abba") == "bba"
    assert longest_substring_with_all_chars("aabb") == "aabb"