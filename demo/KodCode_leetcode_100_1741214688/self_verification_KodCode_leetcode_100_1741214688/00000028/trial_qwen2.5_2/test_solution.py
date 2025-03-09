from solution import *

import pytest
from solution import min_swaps_to_group_ones

def test_min_swaps_to_group_ones():
    assert min_swaps_to_group_ones("11001") == 1
    assert min_swaps_to_group_ones("0011100") == 2
    assert min_swaps_to_group_ones("1111") == 0
    assert min_swaps_to_group_ones("01010101") == 4
    assert min_swaps_to_group_ones("00010001000") == 3
    assert min_swaps_to_group_ones("1001001001") == 3