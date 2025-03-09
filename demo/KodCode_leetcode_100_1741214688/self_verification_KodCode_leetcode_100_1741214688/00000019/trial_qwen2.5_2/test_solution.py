from solution import *

import pytest

def test_find_smallest_substring_empty_string():
    assert find_smallest_substring("") == ""

def test_find_smallest_substring_single_character():
    assert find_smallest_substring("a") == "a"

def test_find_smallest_substring_simple():
    assert find_smallest_substring("baa") == "aab"

def test_find_smallest_substring_repeated_characters():
    assert find_smallest_substring("bbbaaaba") == "aaaaab"

def test_find_smallest_substring_with_lexicographical_check():
    assert find_smallest_substring("abc") == "abc"
    assert find_smallest_substring("dcba") == "abcd"
    assert find_smallest_substring("ababc") == "aabbc"
    assert find_smallest_substring("leetcode") == "cdeo"