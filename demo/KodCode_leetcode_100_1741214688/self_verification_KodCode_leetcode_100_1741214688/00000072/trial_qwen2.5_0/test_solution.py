from solution import *

import pytest

def test_count_split_ways():
    assert count_split_ways("1010") == 1
    assert count_split_ways("001101") == 2
    assert count_split_ways("111") == 0
    assert count_split_ways("0000") == 0  # Invalid as there are no ways to split a string of length less than 6
    assert count_split_ways("101010") == 4