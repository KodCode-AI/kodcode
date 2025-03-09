from solution import *

from solution import count_uppercase

def test_count_uppercase_empty_string():
    assert count_uppercase("") == 0

def test_count_uppercase_no_uppercase_chars():
    assert count_uppercase("hello world") == 0

def test_count_uppercase_mixed_case():
    assert count_uppercase("Hello World") == 2

def test_count_uppercase_all_uppercase():
    assert count_uppercase("HELLO WORLD") == 10

def test_count_uppercase_punctuation():
    assert count_uppercase("Hello, World!") == 2

def test_count_uppercase_num_and_special():
    assert count_uppercase("123!@#ABCDEFG") == 7