from solution import *

from solution import reverse_string

def test_reverse_string_empty():
    assert reverse_string("") == ""

def test_reverse_string_single_character():
    assert reverse_string("a") == "a"

def test_reverse_string_normal():
    assert reverse_string("hello") == "olleh"

def test_reverse_string_with_spaces():
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_string_with_punctuation():
    assert reverse_string("hello, world!") == "!dlrow ,olleh"