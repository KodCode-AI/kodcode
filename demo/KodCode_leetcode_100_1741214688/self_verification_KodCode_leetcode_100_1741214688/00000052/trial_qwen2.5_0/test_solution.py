from solution import *

import pytest

def test_max_balanced_substring_length():
    assert max_balanced_substring_length("00110011", 1) == 6
    assert max_balanced_substring_length("0010", 0) == 2
    assert max_balanced_substring_length("10000", 1) == 4
    assert max_balanced_substring_length("0101010", 2) == 8
    assert max_balanced_substring_length("0001111", 2) == 6
    assert max_balanced_substring_length("0000", 3) == 6
    assert max_balanced_substring_length("11110000", 3) == 6
    assert max_balanced_substring_length("11001100", 1) == 6
    assert max_balanced_substring_length("010101", 0) == 4
    assert max_balanced_substring_length("10101010", 1) == 6
    assert max_balanced_substring_length("111111111", 3) == 9

pytest.main()