from solution import *

import pytest

def test_is_valid_double_positive():
    assert is_valid_double("123.456") == True
    assert is_valid_double("-123.456") == True

def test_is_valid_double_decimal_only():
    assert is_valid_double(".456") == True

def test_is_valid_double_integer():
    assert is_valid_double("123") == False
    assert is_valid_double("-123") == False

def test_is_valid_double_negative():
    assert is_valid_double("-.456") == True

def test_is_valid_double_empty():
    assert is_valid_double("") == False

def test_is_valid_double_special_chars():
    assert is_valid_double("123.456.789") == False
    assert is_valid_double("123..456") == False
    assert is_valid_double("abc") == False
    assert is_valid_double("123..") == False
    assert is_valid_double(".123") == True
    assert is_valid_double("123.") == True