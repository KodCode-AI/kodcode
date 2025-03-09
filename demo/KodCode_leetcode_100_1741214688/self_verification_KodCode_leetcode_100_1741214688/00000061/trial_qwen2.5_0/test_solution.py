from solution import *

def test_max_good_substrings():
    assert max_good_substrings("1001010011", 3) == 3
    assert max_good_substrings("1000", 1) == 1
    assert max_good_substrings("000111000", 2) == 2
    assert max_good_substrings("111", 1) == 1
    assert max_good_substrings("0000000", 4) == 4
    assert max_good_substrings("110010", 2) == 3