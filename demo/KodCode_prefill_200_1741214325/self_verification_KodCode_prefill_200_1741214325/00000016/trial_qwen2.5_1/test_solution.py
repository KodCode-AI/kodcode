from solution import *

from solution import char_counter

def test_char_counter_empty_string():
    assert char_counter("") == (0, 0, 0)

def test_char_counter_with_letters():
    assert char_counter("abcd") == (4, 0, 0)

def test_char_counter_with_digits():
    assert char_counter("12345") == (0, 5, 0)

def test_char_counter_with_special_characters():
    assert char_counter("!@#$%^&*()") == (0, 0, 10)

def test_char_counter_with_mixed_content():
    assert char_counter("abc123!@#") == (3, 3, 3)

def test_char_counter_with_duplicates():
    assert char_counter("aabbccddee112233") == (6, 6, 0)

def test_char_counter_with_punctuation():
    assert char_counter("hello, world!") == (8, 0, 2)