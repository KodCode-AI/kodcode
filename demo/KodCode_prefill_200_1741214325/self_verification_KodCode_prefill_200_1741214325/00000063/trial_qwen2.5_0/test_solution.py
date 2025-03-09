from solution import *

from solution import string_to_list_of_words

def test_string_to_list_of_words_basic():
    assert string_to_list_of_words("hello world") == ["hello", "world"]

def test_string_to_list_of_words_empty():
    assert string_to_list_of_words("") == []

def test_string_to_list_of_words_with_newline():
    assert string_to_list_of_words("split\nnextline") == ["split", "nextline"]

def test_string_to_list_of_words_with_tabs():
    assert string_to_list_of_words("one\ttwo\tthree") == ["one", "two", "three"]

def test_string_to_list_of_words_with_punctuation():
    assert string_to_list_of_words("end.of.sentences,are.detected.automatically") == ["end.of.sentences", "are.detected.automatically"]