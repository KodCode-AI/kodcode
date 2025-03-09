import math
from functools import reduce

def ascii85_encode(data):
    """
    Encodes binary data into Base85 format (Ascii85).
    """
    chunk_size = 4  # 4 bytes per chunk
    encoded = []
    if not data:
        return b''
    
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    
    for chunk in chunks:
        # Convert chunk to integer
        chunk_int = int.from_bytes(chunk, byteorder='big')
        
        # Encode chunk to Base85
        encoded_chars = []
        while chunk_int > 0:
            chunk_int, remainder = divmod(chunk_int, 85)
            encoded_chars.append(chr(33 + remainder))
        encoded.reverse()
        
        # Pad to 5 characters if needed
        while len(encoded_chars) < 5:
            encoded_chars.append('!')
        encoded.append(''.join(encoded_chars))
    
    return ''.join(encoded).encode()

def ascii85_decode(data):
    """
    Decodes Base85 format (Ascii85) back to binary data.
    """
    data = data.decode()
    chunks = [data[i:i+5] for i in range(0, len(data), 5)]
    
    decoded = []
    for chunk in chunks:
        chunk_int = 0
        for i, char in enumerate(chunk):
            if char[0] == '!':
                break
            chunk_int += (85 ** (4 - i)) * (ord(char) - 33)
        
        # Convert integer back to bytes
        byte_ints = bytearray()
        for _ in range(4):
            byte_ints.insert(0, chunk_int & 0xff)
            chunk_int >>= 8
        
        # Handle padding
        while len(byte_ints) < 4:
            byte_ints.insert(0, 0)
        
        decoded.extend(byte_ints)
    
    return bytes(decoded)