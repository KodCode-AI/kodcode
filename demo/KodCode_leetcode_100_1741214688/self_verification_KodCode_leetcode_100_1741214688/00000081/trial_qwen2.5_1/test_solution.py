from solution import *

from solution import longest_substring_with_all_chars

def test_longest_substring_with_all_chars():
    assert longest_substring_with_all_chars("xyyzyzyyx") == "zyzyyx"
    assert longest_substring_with_all_chars("abc") == "abc"
    assert longest_substring_with_all_chars("a") == ""
    assert longest_substring_with_all_chars("bbaaacbb") == "baaacb"
    assert longest_substring_with_all_chars("aabbccddeeff") == "aabbccddeeff"
    assert longest_substring_with_all_chars("abcdef") == "abcdef"
    assert longest_substring_with_all_chars("aaa") == "a"
    assert longest_substring_with_all_chars("aaab") == "aab"
    assert longest_substring_with_all_chars("abcabc") == "abc"