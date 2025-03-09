from solution import *

from solution import extract_shortest_words

def test_extract_shortest_words_single_word():
    assert extract_shortest_words("banana") == {'b': 1, 'a': 1, 'n': 1}

def test_extract_shortest_words_multiple_words():
    assert extract_shortest_words("The quick brown fox") == {'t': 1, 'h': 1, 'e': 1, 'q': 1, 'u': 1, 'k': 1, 'b': 1, 'r': 1, 'w': 1, 'o': 1, 'n': 1, 'f': 1, 'x': 1}

def test_extract_shortest_words_with_punctuation():
    assert extract_shortest_words("A quick, brown; fox!") == {'a': 1, 'q': 1, 'u': 1, 'k': 1, 'i': 1, 'c': 1, 'b': 1, 'r': 1, 'w': 1, 'o': 1, 'n': 1, 'f': 1, 'x': 1}

def test_extract_shortest_words_empty_string():
    assert extract_shortest_words("") == {}

def test_extract_shortest_words_single_word_tuple():
    assert extract_shortest_words("Heavy") == {'h': 1, 'e': 1, 'a': 1, 'v': 1, 'y': 1}

def test_extract_shortest_words_full_sentence():
    assert extract_shortest_words("To be, or not to be, that is the question.") == {'t': 1, 'o': 1, 'b': 1, 'e': 1, 'n': 1, 't': 1, 'q': 1, 'i': 1, 's': 1, 't': 1, 'h': 1, 't': 1, 'a': 1, 't': 1, 's': 1}