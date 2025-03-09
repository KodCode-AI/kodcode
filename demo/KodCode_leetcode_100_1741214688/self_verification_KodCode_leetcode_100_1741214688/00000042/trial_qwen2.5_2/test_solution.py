from solution import *

def test_add_binary():
    assert add_binary("11", "1") == "100"
    assert add_binary("1010", "1011") == "10101"
    assert add_binary("0", "0") == "0"
    assert add_binary("1", "0") == "1"
    assert add_binary("1111", "1111") == "11110"
    assert add_binary("1111", "0001") == "10000"
    assert add_binary("1101", "1011") == "11000"
    assert add_binary("10101", "11111") == "110010"