from solution import *

import string_to_ascii_list

def test_string_to_ascii_list_empty_string():
    assert string_to_ascii_list.string_to_ascii_list("") == []

def test_string_to_ascii_list_single_character():
    assert string_to_ascii_list.string_to_ascii_list("a") == [97]

def test_string_to_ascii_list_multiple_characters():
    assert string_to_ascii_list.string_to_ascii_list("hello") == [104, 101, 108, 108, 111]

def test_string_to_ascii_list_with_spaces():
    assert string_to_ascii_list.string_to_ascii_list("hello world") == [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]