from solution import *

import pytest

def test_min_swaps_to_group_ones():
    assert min_swaps_to_group_ones("10110") == 2
    assert min_swaps_to_group_ones("0011100111") == 4
    assert min_swaps_to_group_ones("1111") == 0
    assert min_swaps_to_group_ones("000") == 0
    assert min_swaps_to_group_ones("110011001110001110") == 6
    assert min_swaps_to_group_ones("10001") == 1
    assert min_swaps_to_group_ones("1101111000110") == 2