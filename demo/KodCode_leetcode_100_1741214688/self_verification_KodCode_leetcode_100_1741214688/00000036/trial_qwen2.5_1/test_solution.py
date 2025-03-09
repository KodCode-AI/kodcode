from solution import *

def test_min_flips_to_alternate():
    assert min_flips_to_alternate("0011") == 2
    assert min_flips_to_alternate("10") == 0
    assert min_flips_to_alternate("1111") == -1
    assert min_flips_to_alternate("0101010") == 0
    assert min_flips_to_alternate("00011000") == 4
    assert min_flips_to_alternate("1100") == 1
    assert min_flips_to_alternate("") == 0