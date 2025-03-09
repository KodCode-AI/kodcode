from solution import *

def test_countGoodSubstrings():
    assert countGoodSubstrings("1001010") == 3
    assert countGoodSubstrings("100010010") == 5
    assert countGoodSubstrings("01010101") == 4
    assert countGoodSubstrings("0000") == 0
    assert countGoodSubstrings("111111") == 3
    assert countGoodSubstrings("00110011") == 6
    assert countGoodSubstrings("10010101010010") == 7

test_countGoodSubstrings()