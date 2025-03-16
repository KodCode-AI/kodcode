from solution import *

import pytest

def test_str_to_int_valid():
    assert str_to_int("42") == 42
    assert str_to_int("   -42") == -42
    assert str_to_int("4193 with words") == 4193

def test_str_to_int_leading_whitespace():
    assert str_to_int("     42") == 42
    assert str_to_int("     -42") == -42

def test_str_to_int_trailing_whitespace():
    assert str_to_int("42   ") == 42
    assert str_to_int("-42   ") == -42

def test_str_to_int_invalid_characters():
    assert str_to_int("4193.23+193") == 4193
    assert str_to_int("words and 987") == 0
    assert str_to_int("-91283472332") == -2147483648  # Lower bound of int32

def test_str_to_int_empty_string():
    assert str_to_int("") == 0

def test_str_to_int_negative_with_space():
    assert str_to_int("  -42abc") == -42

def test_str_to_int_positive_with_space():
    assert str_to_int("  +42abc") == 42

def test_str_to_int_overflow():
    assert str_to_int("2147483648") == 2147483647  # Upper bound of int32
    assert str_to_int("-2147483649") == -2147483648  # Lower bound of int32