from solution import *

from solution import countGoodSubstrings

def test_countGoodSubstrings():
    assert countGoodSubstrings("1001010") == 3
    assert countGoodSubstrings("10") == 0
    assert countGoodSubstrings("1101101100") == 7
    assert countGoodSubstrings("0000") == 0
    assert countGoodSubstrings("1111111111") == 0
    assert countGoodSubstrings("10101010") == 4
    assert countGoodSubstrings("1010101") == 2

if __name__ == "__main__":
    import pytest
    pytest.main()