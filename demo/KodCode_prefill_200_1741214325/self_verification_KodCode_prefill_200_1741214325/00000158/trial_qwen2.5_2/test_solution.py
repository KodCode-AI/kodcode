from solution import *

from solution import count_char_in_string

def test_count_char_in_string_with_matching_chars():
    assert count_char_in_string('a', 'banana') == 3
    assert count_char_in_string('n', 'superman') == 2
    assert count_char_in_string('z', 'zzzzz') == 5

def test_count_char_in_string_with_no_matching_chars():
    assert count_char_in_string('x', 'hello') == 0
    assert count_char_in_string('!', 'abc') == 0

def test_count_char_in_string_with_empty_string():
    assert count_char_in_string('d', '') == 0

def test_count_char_in_string_case_insensitive():
    assert count_char_in_string('a', 'AaAaA') == 3
    assert count_char_in_string('A', 'AaAaA') == 3

def test_count_char_in_string_space():
    assert count_char_in_string(' ', 'Hello world') == 1