from solution import *

from solution import decimal_to_binary

def test_decimal_to_binary():
    assert decimal_to_binary(10) == "1010"
    assert decimal_to_binary(0) == "0"
    assert decimal_to_binary(19) == "10011"
    assert decimal_to_binary(255) == "11111111"
    assert decimal_to_binary(4095) == "111111111111"
    assert decimal_to_binary(2) == "10"
    assert decimal_to_binary(1) == "1"
    assert decimal_to_binary(2147483647) == "1111111111111111111111111111111"