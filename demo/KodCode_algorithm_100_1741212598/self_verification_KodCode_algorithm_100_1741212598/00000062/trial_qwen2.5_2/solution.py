import math

def ascii85_encode(data: bytes) -> bytes:
    """Encodes the binary data to Ascii85 format."""
    chunk_size = 4
    chunk_count = math.ceil(len(data) / chunk_size)
    encoded = b""
    for i in range(chunk_count):
        chunk = data[i*chunk_size:(i+1)*chunk_size]
        while len(chunk) < 4:
            chunk += b'\x00'
        chunk_int = int.from_bytes(chunk, byteorder='Big')
        for j in range(5):
            pos = 84 ** (4 - j - 1)
            encoded += bytes([min(chunk_int // pos, 85)])
            chunk_int %= pos
    return encoded

def ascii85_decode(data: bytes) -> bytes:
    """Decodes the Base85 encoded data back to binary data."""
    chunk_size = 5
    chunk_count = math.ceil(len(data) / chunk_size)
    decoded = b""
    for i in range(chunk_count):
        chunk = data[i*chunk_size:(i+1)*chunk_size]
        if not chunk:
            continue
        chunk_int = 0
        for j, byte in enumerate(chunk):
            chunk_int += (85 ** (4 - j)) * (byte - 33)
        for j in range(4):
            pos = 85 ** (4 - j - 1)
            decoded += bytes([chunk_int // pos].to_bytes(1, byteorder='Big'))
            chunk_int %= pos
    return decoded[:-1 if decoded[-1:] == b'\x00' else 0]