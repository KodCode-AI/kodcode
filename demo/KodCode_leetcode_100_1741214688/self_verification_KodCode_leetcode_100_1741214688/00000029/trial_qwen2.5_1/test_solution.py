from solution import *

def test_longest_balanced_substring():
    assert longest_balanced_substring("100110", 2) == 8
    assert longest_balanced_substring("1010", 0) == 4
    assert longest_balanced_substring("010101", 1) == 6
    assert longest_balanced_substring("1100011", 2) == 7
    assert longest_balanced_substring("10001000", 1) == 6
    assert longest_balanced_substring("0101", 3) == 6
    assert longest_balanced_substring("0001111000011110000000011110000", 5) == 16