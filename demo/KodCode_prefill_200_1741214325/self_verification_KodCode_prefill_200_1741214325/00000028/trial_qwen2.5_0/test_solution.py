from solution import *

import pytest

def test_is_valid_double():
    assert is_valid_double("123.456") == True
    assert is_valid_double("-123.456") == True
    assert is_valid_double("+123.456") == True
    assert is_valid_double("123") == True
    assert is_valid_double(".456") == True
    assert is_valid_double("123.") == True
    assert is_valid_double("123.456e-7") == True
    assert is_valid_double("123.456E7") == True
    assert is_valid_double("123.456e+7") == True
    assert is_valid_double("123.456E+7") == True
    assert is_valid_double("123.") == True
    assert is_valid_double(".123") == True
    assert is_valid_double("123.123.123") == False
    assert is_valid_double("abc") == False
    assert is_valid_double("") == False
    assert is_valid_double("123e") == False
    assert is_valid_double("e123") == False
    assert is_valid_double("123e5.45") == False
    assert is_valid_double("--123.456") == False
    assert is_valid_double("-+123.456") == False