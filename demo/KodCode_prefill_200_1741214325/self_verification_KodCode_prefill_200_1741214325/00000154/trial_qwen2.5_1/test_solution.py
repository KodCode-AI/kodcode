from solution import *

from solution import split_string_into_words

def test_split_string_into_words():
    test_string = "Hello, world. This is a test."
    expected_output = ["Hello", "world", "This", "is", "a", "test"]
    assert split_string_into_words(test_string) == expected_output

def test_split_string_with_multiple_delimiters():
    test_string = "One, two, three. Four five six"
    expected_output = ["One", "two", "three", "Four", "five", "six"]
    assert split_string_into_words(test_string) == expected_output

def test_split_empty_string():
    test_string = ""
    expected_output = []
    assert split_string_into_words(test_string) == expected_output

def test_split_string_with_no_delimiters():
    test_string = "OnetwothreeFourfivesix"
    expected_output = ["OnetwothreeFourfivesix"]
    assert split_string_into_words(test_string) == expected_output

def test_split_string_with_only_delimiters():
    test_string = ",,.   ...  "
    expected_output = []
    assert split_string_into_words(test_string) == expected_output

def test_split_string_with_tab_and_newline():
    test_string = "Line1\tLine2\nLine3"
    expected_output = ["Line1", "Line2", "Line3"]
    assert split_string_into_words(test_string) == expected_output