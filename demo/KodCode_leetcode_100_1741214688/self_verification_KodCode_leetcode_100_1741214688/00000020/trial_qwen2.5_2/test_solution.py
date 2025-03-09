from solution import *

import pytest

def test_max_length_simple_case():
    assert max_length("110") == 3

def test_max_length_all_zeros():
    assert max_length("000") == 3

def test_max_length_all_ones():
    assert max_length("111") == 3

def test_max_length_complex_case():
    assert max_length("1001010") == 5

def test_max_length_single_character():
    assert max_length("1") == 1

def test_max_length_with_initial_0():
    assert max_length("01100110") == 8

def test_max_length_with_alternating_01():
    assert max_length("01010101") == 4

def test_max_length_empty_string():
    assert max_length("") == 0

def test_max_length_long_string():
    assert max_length("11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111") == 32