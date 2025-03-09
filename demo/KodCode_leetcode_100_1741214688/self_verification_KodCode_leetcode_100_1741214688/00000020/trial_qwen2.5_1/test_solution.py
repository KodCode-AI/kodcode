from solution import *

def test_max_length_without_010():
    assert max_length_without_010("110") == 3
    assert max_length_without_010("0001010111") == 9
    assert max_length_without_010("1010101010") == 5
    assert max_length_without_010("1111111111") == 10
    assert max_length_without_010("0101010101") == 5
    assert max_length_without_010("1110101110") == 8
    assert max_length_without_010("000") == 3
    assert max_length_without_010("1111") == 4