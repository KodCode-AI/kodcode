from solution import *

from solution import length_of_longest_substring

def test_length_of_longest_substring_empty_string():
    assert length_of_longest_substring("") == 0

def test_length_of_longest_substring_single_character():
    assert length_of_longest_substring("a") == 1

def test_length_of_longest_substring_without_repeating_characters():
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3

def test_length_of_longest_substring_with_repeating_characters():
    assert length_of_longest_substring("dvdf") == 3
    assert length_of_longest_substring("abba") == 2
    assert length_of_longest_substring("tmmzuxt") == 5