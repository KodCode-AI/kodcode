from solution import *

from solution import add_binary

def test_add_binary_positive_cases():
    assert add_binary("11", "1") == "100"
    assert add_binary("1010", "1011") == "10101"

def test_add_binary_with_zeros():
    assert add_binary("0", "0") == "0"
    assert add_binary("0", "1") == "1"
    assert add_binary("1", "0") == "1"

def test_add_binary_with_large_numbers():
    assert add_binary("1111111111", "1") == "10000000000"
    assert add_binary("10000000001000000000", "10000000001000000000") == "10000000001000000000000000000"

def test_add_binary_negative_cases():
    assert add_binary("0", "10") == "10"
    assert add_binary("10", "0") == "10"