from solution import *

def test_decimal_to_binary():
    assert decimal_to_binary(0) == '0'
    assert decimal_to_binary(1) == '1'
    assert decimal_to_binary(2) == '10'
    assert decimal_to_binary(3) == '11'
    assert decimal_to_binary(4) == '100'
    assert decimal_to_binary(5) == '101'
    assert decimal_to_binary(14) == '1110'
    assert decimal_to_binary(255) == '11111111'
    assert decimal_to_binary(256) == '100000000'
    assert decimal_to_binary(1023) == '1111111111'

def test_single_digit():
    assert decimal_to_binary(1) == '1'
    assert decimal_to_binary(9) == '1001'