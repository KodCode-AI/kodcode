from solution import *

from solution import filter_words

def test_filter_words_no_substring():
    assert filter_words(["hello", "world", "python"], "a") == ["hello", "world", "python"]

def test_filter_words_with_substring():
    assert filter_words(["apple", "banana", "grape", "peach"], "a") == ["grape", "peach"]

def test_filter_words_empty_list():
    assert filter_words([], "test") == []

def test_filter_words_all_match():
    assert filter_words(["test", "blast", "pasta"], "st") == ["pasta"]

def test_filter_words_caseInsensitive():
    assert filter_words(["Apple", "banana", "grape"], "a") == ["banana", "grape"]