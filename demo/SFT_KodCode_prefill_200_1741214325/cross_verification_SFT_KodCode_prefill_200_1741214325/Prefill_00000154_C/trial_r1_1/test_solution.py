from solution import *

def test_split_string_into_words():
    assert split_string_into_words("Hello, world. This is a test.") == ["Hello", "world", "This", "is", "a", "test"]
    assert split_string_into_words("Split,these,words,using,multiple,delimiters.") == ["Split", "these", "words", "using", "multiple", "delimiters"]
    assert split_string_into_words("NoDelimitersHere") == ["NoDelimitersHere"]
    assert split_string_into_words("Trailing,separator,") == ["Trailing", "separator"]
    assert split_string_into_words("Leading,separator,,Leading,combinations,of,delimiters., ") == ["Leading", "separator", "Leading", "combinations", "of", "delimiters"]