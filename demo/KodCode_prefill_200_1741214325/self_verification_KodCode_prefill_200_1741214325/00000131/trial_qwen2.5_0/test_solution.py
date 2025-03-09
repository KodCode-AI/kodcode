from solution import *

import pytest

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("12345") == "54321"
    assert reverse_string("") == ""

def test_reverse_integer_sequence():
    assert reverse_string("123456789") == "987654321"
    assert reverse_string("0") == "0"

def test_reverse_special_characters():
    assert reverse_string("!@#$%^&*()") == ")(*&^%$#@!"

def test_reverse mixed_case():
    assert reverse_string("Hello World!") == "!dlroW olleH"
    assert reverse_string("1a2b3c") == "c3b2a1"