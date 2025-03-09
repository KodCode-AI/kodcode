from solution import *

def test_count_lychrel():
    assert count_lychrel(10000) == 249
    assert count_lychrel(2000) == 106
    assert count_lychrel(1000) == 52
    assert count_lychrel(100) == 19
    assert count_lychrel(100000) == 24960
    assert count_lychrel(1) == 0