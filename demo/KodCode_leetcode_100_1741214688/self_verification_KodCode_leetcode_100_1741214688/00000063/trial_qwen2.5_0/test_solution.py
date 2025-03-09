from solution import *

def test_min_operations_to_k_ones():
    assert min_operations_to_k_ones("0001000", 3) == 3
    assert min_operations_to_k_ones("10000000000", 3) == 3
    assert min_operations_to_k_ones("111", 1) == 1
    assert min_operations_to_k_ones("0000000000", 1) == 9
    assert min_operations_to_k_ones("0011001100", 5) == 1
    assert min_operations_to_k_ones("0101010101", 5) == 5
    assert min_operations_to_k_ones("1111111111", 10) == 0