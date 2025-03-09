from solution import *

def test_decimal_to_binary():
    assert decimal_to_binary(0) == "0"
    assert decimal_to_binary(1) == "1"
    assert decimal_to_binary(5) == "101"
    assert decimal_to_binary(10) == "1010"
    assert decimal_to_binary(255) == "11111111"
    assert decimal_to_binary(256) == "100000000"