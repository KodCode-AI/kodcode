from solution import *

import pytest

def test_max_good_substrings():
    assert max_good_substrings("1001010011", 3) == 3
    assert max_good_substrings("100011000", 1) == 2
    assert max_good_substrings("101010101", 2) == 4
    assert max_good_substrings("0001", 3) == 1
    assert max_good_substrings("111100000", 5) == 5
    assert max_good_substrings("010101010", 8) == 8