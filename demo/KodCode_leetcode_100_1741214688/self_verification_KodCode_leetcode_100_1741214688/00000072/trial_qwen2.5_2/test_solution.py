from solution import *

def test_count_good_splits():
    assert count_good_splits("1010") == 2
    assert count_good_splits("001101") == 1
    assert count_good_splits("111") == 0
    assert count_good_splits("000") == 0
    assert count_good_splits("110101") == 3