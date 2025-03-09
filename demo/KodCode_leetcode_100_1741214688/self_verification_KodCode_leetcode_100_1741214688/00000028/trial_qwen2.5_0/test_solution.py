from solution import *

def test_min_swaps_to_group_ones():
    assert min_swaps_to_group_ones("110") == 1
    assert min_swaps_to_group_ones("0011100") == 1
    assert min_swaps_to_group_ones("1000110001") == 3
    assert min_swaps_to_group_ones("1010101010") == 0
    assert min_swaps_to_group_ones("1110000111") == 0
    assert min_swaps_to_group_ones("0101010101") == 5