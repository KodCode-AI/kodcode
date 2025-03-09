from solution import *

from solution import count_char_in_string

def test_count_char_in_string():
    assert count_char_in_string("hello world", "l") == 3
    assert count_char_in_string("aaaabbb", "a") == 4
    assert count_char_in_string("python programming", "p") == 2
    assert count_char_in_string("test case", "z") == 0

def test_count_char_in_empty_string():
    assert count_char_in_string("", "a") == 0

def test_count_char_case_insensitive():
    assert count_char_in_string("Hello World", "h") == 1