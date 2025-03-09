from solution import *

from solution import char_frequency

def test_char_frequency_empty_string():
    assert char_frequency("") == {}

def test_char_frequency_single_character():
    assert char_frequency("a") == {'a': 1}

def test_char_frequency_multiple_characters():
    assert char_frequency("aabbc") == {'a': 2, 'b': 2, 'c': 1}

def test_char_frequency_with_spaces():
    assert char_frequency("hello world") == {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

def test_char_frequency_with_special_characters():
    assert char_frequency("!!@#$%^&*()_+") == {'!': 2, '@': 1, '#': 1, '$': 1, '%': 1, '^': 1, '&': 1, '*': 1, '(': 1, ')': 1, '_': 1, '+': 1}