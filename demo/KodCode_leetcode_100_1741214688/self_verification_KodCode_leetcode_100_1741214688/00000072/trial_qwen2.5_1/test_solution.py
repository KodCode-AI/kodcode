from solution import *

def test_count_split_ways():
    assert count_split_ways("1010") == 2
    assert count_split_ways("1001") == 1
    assert count_split_ways("111") == 0
    assert count_split_ways("0101010") == 6
    assert count_split_ways("0000") == 0