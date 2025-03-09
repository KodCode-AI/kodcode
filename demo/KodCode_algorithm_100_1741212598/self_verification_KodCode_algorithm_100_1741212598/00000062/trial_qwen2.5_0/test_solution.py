from solution import *

import base64

def test_ascii85_encode_decode():
    test_bytes = b'12345'
    encoded = ascii85_encode(test_bytes)
    decoded = ascii85_decode(encoded)
    assert base64.b85encode(test_bytes) == encoded
    assert test_bytes == decoded

def test_ascii85_decode_null():
    assert ascii85_decode(b'') == b''

def test_ascii85_encode_empty():
    assert ascii85_encode(b'') == b''

def test_ascii85_decode_padding():
    for padding in ['!!!!', '!']:
        encoded = ascii85_encode(b'12345')
        encoded = encoded.decode().replace('!etOA2#', padding)
        decoded = ascii85_decode(encoded.encode())
        assert b'12345' == decoded

def test_ascii85_encode_padding():
    encoded = b'!etOA2!R@3Dfsd'
    decoded = ascii85_decode(encoded)
    assert b'12345' == decoded

def test_ascii85_large_data():
    large_data = os.urandom(1024 * 1024)  # 1MB of random data
    encoded = ascii85_encode(large_data)
    decoded = ascii85_decode(encoded)
    assert large_data == decoded