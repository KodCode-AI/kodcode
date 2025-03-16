from solution import *

from solution import char_count

def test_char_count_single_character():
    assert char_count("hello", "l") == 2

def test_char_count_multiple_characters():
    assert char_count("banana", "a") == 3

def test_char_count_empty_string():
    assert char_count("", "a") == 0

def test_char_count_with_whitespace():
    assert char_count("hello world", " ") == 1

def test_char_count_case_sensitive():
    assert char_count("Hello", "h") == 0
    assert char_count("Hello", "H") == 1

def test_char_count_special_characters():
    assert char_count("hello@world", "@") == 1