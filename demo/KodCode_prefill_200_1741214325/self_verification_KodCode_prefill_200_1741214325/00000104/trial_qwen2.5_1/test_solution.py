from solution import *

import pytest

def test_is_valid_identifier():
    assert is_valid_identifier("var1") == True
    assert is_valid_identifier("_myVar") == True
    assert is_valid_identifier("99vars") == False
    assert is_valid_identifier("xyz!") == False
    assert is_valid_identifier("valid_identifier123") == True
    assert is_valid_identifier("class_name") == False  # Does not start with a lowercase letter

def test_is_valid_with_digits():
    assert is_valid_identifier("var_123") == True
    assert is_valid_identifier("123Var") == False

def test_is_valid_with_special_chars():
    assert is_valid_identifier("_") == True
    assert is_valid_identifier("__") == True
    assert is_valid_identifier("___") == True
    assert is_valid_identifier("_123") == True
    assert is_valid_identifier("123_") == False

def test_is_valid_with_underscore_within():
    assert is_valid_identifier("valid_var_name") == True
    assert is_valid_identifier("valid_var_name_") == True

def test_is_valid_empty_string():
    assert is_valid_identifier("") == False

def test_is_valid_starting_with_digit():
    assert is_valid_identifier("123valid") == False