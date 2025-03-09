from solution import *

from solution import reverse_string

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("12345") == "54321"

def test_reverse_integer_sequence():
    assert reverse_string(12345) == "54321"
    
def test_reverse_empty_string():
    assert reverse_string("") == ""
    
def test_reverse_single_character():
    assert reverse_string("a") == "a"

def test_reverse_special_characters():
    assert reverse_string("!@#$") == "$#@$!"