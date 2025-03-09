from solution import *

import pytest
from solution import ascii85_encode, ascii85_decode

def test_ascii85_encode_decode():
    assert ascii85_decode(ascii85_encode(b"12345")) == b"12345"

def test_ascii85_encode_decode_empty():
    assert ascii85_decode(ascii85_encode(b"")) == b""

def test_ascii85_encode_decode_spaces():
    assert ascii85_decode(ascii85_encode(b"  test  ")) == b"  test  "

def test_ascii85_encode_decode_punctuation():
    assert ascii85_decode(ascii85_encode(b"!@#$%^&*()")) == b"!@#$%^&*()"

def test_ascii85_encode_decode_long():
    long_string = b"This is a very long string of text to test the encode and decode functions of Base85 encoding."
    encoded = ascii85_encode(long_string)
    decoded = ascii85_decode(encoded)
    assert decoded == long_string

def test_ascii85_encode_decode_combined():
    test_data = b"1234567890\x01\x02\x03\x04\x05\x06\x07\x08"
    encoded = ascii85_encode(test_data)
    decoded = ascii85_decode(encoded)
    assert decoded == test_data