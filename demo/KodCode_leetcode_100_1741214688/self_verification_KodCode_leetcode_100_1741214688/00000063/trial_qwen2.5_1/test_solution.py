from solution import *

def test_min_operations_to_k_ones():
    assert min_operations_to_k_ones("00010101001", 3) == 3
    assert min_operations_to_k_ones("0101010", 1) == 2
    assert min_operations_to_k_ones("111000", 3) == 0
    assert min_operations_to_k_ones("00", 1) == 1
    assert min_operations_to_k_ones("1111111", 5) == 6

def test_min_operations_with_large_input():
    input_str = '0' * 100 + '1' * 100 + '0' * 100 + '1' * 100
    assert min_operations_to_k_ones(input_str, 200) == 1