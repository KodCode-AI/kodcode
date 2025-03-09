from solution import *

import re
from solution import replace_surrounded_substring

def test_replace_surrounded_substring():
    test_text = "hello world, this is a test sentence with the word hello"
    assert replace_surrounded_substring(test_text, "hello", "goodbye") == "goodbye world, this is a test sentence with the word goodbye"

def test_no_change_if_not_surrounded():
    test_text = "hel lo world, this is a test sen tence with the word hello"
    assert replace_surrounded_substring(test_text, "hello", "goodbye") == test_text

def test_case_sensitivity():
    test_text = "hello World, this is a test sentence with the word hello"
    assert replace_surrounded_substring(test_text, "hello", "goodbye") == "goodbye World, this is a test sentence with the word goodbye"

def test_multiple_occurrences():
    test_text = "hello hello hello, this is a test sentence with the words hello and goodbye"
    assert replace_surrounded_substring(test_text, "hello", "goodbye") == "goodbye goodbye goodbye, this is a test sentence with the words goodbye and goodbye"

def test_replacement_with_same_substring():
    test_text = "hello hello hello, this is a test sentence with the words hello and goodbye"
    assert replace_surrounded_substring(test_text, "hello", "hello") == test_text

def test_replacement_with_empty_string():
    test_text = "hello world, this is a test sentence with the word hello"
    assert replace_surrounded_substring(test_text, "hello", "") == " world, this is a test sentence with the word "

def test_replacement_with_space():
    test_text = "hello world, this is a test sentence with the word hello"
    assert replace_surrounded_substring(test_text, "hello", " ") == " world, this is a test sentence with the word  "