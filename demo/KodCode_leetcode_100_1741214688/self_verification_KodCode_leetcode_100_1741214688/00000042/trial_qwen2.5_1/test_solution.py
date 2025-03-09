from solution import *

from solution import add_binary

def test_add_binary_positive():
    assert add_binary("11", "1") == "100"

def test_add_binary_single_digit():
    assert add_binary("0", "0") == "0"

def test_add_binary_mixed():
    assert add_binary("1010", "1011") == "10101"

def test_add_binary_large_numbers():
    assert add_binary("11111111111111111111111111111101", "1") == "100000000000000000000000000000000"