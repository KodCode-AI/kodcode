from solution import *

import pytest

def test_str_to_int_positive():
    assert str_to_int("42") == 42
    assert str_to_int('0000042') == 42

def test_str_to_int_negative():
    assert str_to_int("-42") == -42
    assert str_to_int("-12345678901234567890") == -2147483648  # INT_MIN

def test_invalid_characters():
    assert str_to_int("   123abc") == 123
    assert str_to_int("abc123") == 0  # No valid digit at the start

def test_empty_string():
    assert str_to_int("") == 0

def test_trailing_whitespace():
    assert str_to_int("  -42") == -42

def test_leading_whitespace():
    assert str_to_int("42   ") == 42