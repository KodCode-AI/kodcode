from solution import *

from solution import string_to_list_of_words

def test_string_to_list_of_words_single_word():
    assert string_to_list_of_words("hello") == ["hello"]

def test_string_to_list_of_words_multiple_words():
    assert string_to_list_of_words("hello world") == ["hello", "world"]

def test_string_to_list_of_words_with_punctuation():
    assert string_to_list_of_words("hello, world!") == ["hello,", "world!"]

def test_string_to_list_of_words_empty_string():
    assert string_to_list_of_words("") == []

def test_string_to_list_of_words_with_spaces():
    assert string_to_list_of_words("  hello  world  ") == ["hello", "world"]