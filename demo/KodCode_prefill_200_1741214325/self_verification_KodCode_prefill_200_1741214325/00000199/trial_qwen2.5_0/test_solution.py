from solution import *

from solution import longest_substring_without_repeating

def test_longest_substring_with_empty_string():
    assert longest_substring_without_repeating("") == ""

def test_longest_substring_single_character():
    assert longest_substring_without_repeating("a") == "a"

def test_longest_substring_no_repeating_characters():
    assert longest_substring_without_repeating("abcd") == "abcd"

def test_longest_substring_repeating_characters():
    assert longest_substring_without_repeating("abcabcbb") == "abc"
    assert longest_substring_without_repeating("bbbbb") == "b"
    assert longest_substring_without_repeating("pwwkew") == "wke"

def test_longest_substring_with_spaces():
    assert longest_substring_without_repeating(" ") == " "
    assert longest_substring_without_repeating("a a") == " a"
    assert longest_substring_without_repeating("a b a") == " b"