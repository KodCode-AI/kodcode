from solution import *

import re
from solution import is_valid_double

def test_is_valid_double_positive_numbers():
    assert is_valid_double("123.456") == True

def test_is_valid_double_negative_numbers():
    assert is_valid_double("-123.456") == True

def test_is_valid_double_numbers_with_exponent():
    assert is_valid_double("123.456e-2") == True
    assert is_valid_double("-123.456E+2") == True

def test_is_valid_double_invalid_exponent():
    assert is_valid_double("123.e.2") == False

def test_is_valid_double_additional_characters():
    assert is_valid_double(".123") == True
    assert is_valid_double("123.") == True
    assert is_valid_double("123.0") == True
    assert is_valid_double("123e") == False
    assert is_valid_double("abc123.456") == False
    assert is_valid_double("123.456abc") == False

def test_is_valid_double_edge_cases():
    assert is_valid_double("") == False
    assert is_valid_double("e123") == False
    assert is_valid_double(".e123") == False
    assert is_valid_double("123.e") == False
    assert is_valid_double("123e.") == False
    assert is_valid_double("+123.456") == True
    assert is_valid_double("-.456") == True
    assert is_valid_double(".") == False