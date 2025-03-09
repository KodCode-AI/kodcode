from solution import *

import pytest

def test_count_good_substrings():
    assert count_good_substrings("1001010") == 3
    assert count_good_substrings("1100011") == 4
    assert count_good_substrings("0000") == 0
    assert count_good_substrings("1111") == 1
    assert count_good_substrings("10101010") == 8