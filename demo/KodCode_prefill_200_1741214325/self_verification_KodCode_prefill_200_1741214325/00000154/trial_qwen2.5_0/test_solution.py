from solution import *

from solution import split_string_into_words

def test_split_string_into_words():
    assert split_string_into_words("Hello, world. This is a test.") == ["Hello", "world", "This", "is", "a", "test"]
    assert split_string_into_words("Split,these,words...using,.delimiters") == ["Split", "these", "words", "using", "delimiters"]
    assert split_string_into_words("OneWord") == ["OneWord"]
    assert split_string_into_words(",,,.  ..") == []
    assert split_string_into_words("") == []
    assert split_string_into_words("a,b.c d") == ["a", "b", "c", "d"]