from solution import *

import pytest
from solution import ascii85_encode, ascii85_decode

def test_ascii85_encode_decode():
    assert ascii85_decode(ascii85_encode(b"12345")) == b"12345"
    assert ascii85_decode(ascii85_encode(b"onetwothree")) == b"onetwothree"
    assert ascii85_decode(ascii85_encode(b"")) == b""
    assert ascii85_decode(ascii85_encode(b"hello world")) == b"hello world"

def test_ascii85_decode_encode_cycle():
    for _ in range(100):
        original_data = bytearray(b"".join([bytes([i % 256]) for i in range(100000)]))
        encoded = ascii85_encode(original_data)
        decoded = ascii85_decode(encoded)
        assert decoded == original_data

def test_ascii85_edge_cases():
    assert ascii85_encode(b"1234567890") == b"0etOA!-"
    assert ascii85_decode(b"0etOA!-") == b"1234567890"
    assert ascii85_encode(b"") == b""
    assert ascii85_decode(b"") == b""

def test_ascii85_padding():
    assert ascii85_decode(ascii85_encode(b"testing123")) == b"testing123"
    assert ascii85_decode(ascii85_encode(b"123456789012345678901234567890")) == b"123456789012345678901234567890"

def test_ascii85_large_data():
    large_data = b"".join([bytes([i % 256]) for i in range(1000000)])
    encoded = ascii85_encode(large_data)
    assert len(encoded) == len(large_data) // 5 * 85 + len(large_data) % 5 * (85 // 5 + 1)
    decoded = ascii85_decode(encoded)
    assert decoded == large_data

def test_ascii85_decode_rejection_of_invalid_ascii85_strings():
    with pytest.raises(Exception):
        ascii85_decode(b"invalid ascii85")
    with pytest.raises(Exception):
        ascii85_decode(b"123456")
    with pytest.raises(Exception):
        ascii85_decode(b"12345")
    with pytest.raises(Exception):
        ascii85_decode(b"1234567")