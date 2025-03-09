from solution import *

import pytest

def test_max_good_substrings():
    assert max_good_substrings("1001010011", 3) == 3
    assert max_good_substrings("1000", 1) == 2
    assert max_good_substrings("100010001000", 3) == 6
    assert max_good_substrings("1111", 2) == 3
    assert max_good_substrings("101010", 4) == 4
    assert max_good_substrings("101010", 2) == 3
    assert max_good_substrings("1111111", 2) == 2
    assert max_good_substrings("0000", 3) == 3

pytest.main(["-v", __file__])