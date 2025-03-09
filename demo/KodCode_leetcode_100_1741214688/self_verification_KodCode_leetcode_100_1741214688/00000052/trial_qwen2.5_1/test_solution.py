from solution import *

def test_max_balanced_substring_length():
    assert max_balanced_substring_length("010", 1) == 4
    assert max_balanced_substring_length("0011", 2) == 6
    assert max_balanced_substring_length("00110011", 1) == 6
    assert max_balanced_substring_length("01010101", 2) == 8
    assert max_balanced_substring_length("11111111", 10) == 0