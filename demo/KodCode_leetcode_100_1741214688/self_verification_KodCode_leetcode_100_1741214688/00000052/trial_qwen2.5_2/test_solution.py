from solution import *

import pytest

def test_max_balanced_substring_length():
    assert max_balanced_substring_length("00110011", 1) == 6
    assert max_balanced_substring_length("00110011101111", 4) == 12
    assert max_balanced_substring_length("00000", 3) == 2
    assert max_balanced_substring_length("111111", 2) == 4
    assert max_balanced_substring_length("11000", 0) == 0
    assert max_balanced_substring_length("00110011", 0) == 4
    assert max_balanced_substring_length("11110000", 1) == 6
    assert max_balanced_substring_length("01010101", 2) == 8

def test_single_character():
    assert max_balanced_substring_length("1", 1) == 2

def test_all_zeros_with_flips():
    assert max_balanced_substring_length("0000", 3) == 6