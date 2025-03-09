from solution import *

from solution import string_to_list_of_words

def test_string_to_list_of_words_simple():
    assert string_to_list_of_words("hello world") == ['hello', 'world']

def test_string_to_list_of_words_with_punctuation():
    assert string_to_list_of_words("hello, world!") == ['hello', 'world!']

def test_string_to_list_of_words_empty_string():
    assert string_to_list_of_words("") == []

def test_string_to_list_of_words_multiple_spaces():
    assert string_to_list_of_words("hello  world") == ['hello', 'world']

def test_string_to_list_of_words_newline():
    assert string_to_list_of_words("hello\nworld") == ['hello', 'world']