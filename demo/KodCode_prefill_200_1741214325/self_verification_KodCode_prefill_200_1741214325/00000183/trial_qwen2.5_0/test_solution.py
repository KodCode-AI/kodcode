from solution import *

from solution import reverse_string

def test_reverse_string_empty():
    assert reverse_string("") == ""

def test_reverse_string_single_char():
    assert reverse_string("a") == "a"

def test_reverse_string Normal():
    assert reverse_string("hello") == "olleh"

def test_reverse_string_with_spaces():
    assert reverse_string("a b c") == "c b a"

def test_reverse_string_special_chars():
    assert reverse_string("!@#$%^&*()") == ")(*&^%$#@!"