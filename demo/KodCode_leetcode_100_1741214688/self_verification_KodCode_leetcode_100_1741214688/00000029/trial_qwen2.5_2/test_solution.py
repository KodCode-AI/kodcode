from solution import *

def test_longest_balanced_substring():
    assert longest_balanced_substring("1100011", 2) == 7
    assert longest_balanced_substring("1010100", 1) == 6
    assert longest_balanced_substring("000101010", 2) == 8
    assert longest_balanced_substring("0010", 1) == 4
    assert longest_balanced_substring("11010001010010110", 5) == 13

# Additional edge case
def test_empty_string():
    assert longest_balanced_substring("", 0) == 0

# Case with all zeros
def test_all_zeros():
    assert longest_balanced_substring("0000", 1) == 4

# Case with all ones
def test_all_ones():
    assert longest_balanced_substring("1111", 1) == 2

# Case with a balanced string
def test_balanced_string():
    assert longest_balanced_substring("11010101", 0) == 2