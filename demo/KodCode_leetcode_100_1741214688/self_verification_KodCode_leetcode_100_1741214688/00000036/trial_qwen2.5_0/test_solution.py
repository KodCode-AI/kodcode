from solution import *

def test_min_operations_to_alternate():
    assert min_operations_to_alternate("001") == 1
    assert min_operations_to_alternate("10") == 0
    assert min_operations_to_alternate("1111") == -1
    assert min_operations_to_alternate("0101010") == 0
    assert min_operations_to_alternate("00010001") == 2
    assert min_operations_to_alternate("1110000") == 3