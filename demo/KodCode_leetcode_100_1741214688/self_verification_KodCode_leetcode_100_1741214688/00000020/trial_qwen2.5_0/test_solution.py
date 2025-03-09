from solution import *

import pytest

def test_max_length_no_010():
    assert max_length_no_010("110") == 3
    assert max_length_no_010("000") == 3
    assert max_length_no_010("01010101010") == 10
    assert max_length_no_010("1000000") == 7
    assert max_length_no_010("0110000") == 6
    assert max_length_no_010("11111111111111111111111111") == 20
    assert max_length_no_010("10101010101010101010101010") == 10
    assert max_length_no_010("00110011001100110011") == 18