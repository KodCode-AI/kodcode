from solution import *

from solution import shortest_words

def test_shortest_words_empty_string():
    assert shortest_words("") == []

def test_shortest_words_single_word():
    assert shortest_words("hello") == ["hello"]

def test_shortest_words_with_multiple_words():
    assert shortest_words("hello world a ab") == ["a", "ab"]
    assert shortest_words("one two three four seven") == ["one", "two", "three", "four"]

def test_shortest_words_multiple_shortest_words_same_length():
    assert shortest_words("aaa bb cc") == ["aaa", "bb", "cc"]