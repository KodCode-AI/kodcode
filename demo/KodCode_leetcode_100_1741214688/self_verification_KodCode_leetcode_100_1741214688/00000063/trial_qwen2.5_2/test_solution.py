from solution import *

def test_min_operations_to_k_ones():
    assert min_operations_to_k_ones("0001000", 2) == 1
    assert min_operations_to_k_ones("10001000", 2) == 2
    assert min_operations_to_k_ones("0000000", 0) == 0
    assert min_operations_to_k_ones("111111", 6) == 0
    assert min_operations_to_k_ones("001100110011", 3) == 3
    assert min_operations_to_k_ones("001100110011", 4) == 2