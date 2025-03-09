def ascii85_encode(data: bytes) -> bytes:
    """
    Encodes a bytes object into Base85 format.
    """
    encoded_chars = []
    chars = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    acc, count = 0, 0
    for char in data:
        acc = acc * 256 + char
        count += 1
        if count == 5:
            encoded_chars.append(chars[(acc >> 3 * 8) & 0x1f])
            encoded_chars.append(chars[(acc >> 2 * 8) & 0x1f])
            encoded_chars.append(chars[(acc >> 1 * 8) & 0x1f])
            encoded_chars.append(chars[(acc >> 0 * 8) & 0x1f])
            acc, count = 0, 0
    if count:
        rem = 8 * count
        encoded_chars.append(chars[(acc >> (rem - 8 * 2)) & 0x3f])
        if count > 1:
            encoded_chars.append(chars[(acc >> (rem - 8 * 1)) & 0x1f])
        if count > 2:
            encoded_chars.append(chars[(acc >> (rem - 8 * 0)) & 0x0f])
    return "".join(encoded_chars).encode("ascii")

def ascii85_decode(encoded_data: bytes) -> bytes:
    """
    Decodes a Base85 encoded bytes object back to the original binary data.
    """
    encoded_chars = encoded_data.decode("ascii")
    acc, count = 0, 0
    data = bytearray()
    for char in encoded_chars:
        if char == chars[0]:
            data.append(acc)
            acc, count = 0, 0
            continue
        acc = acc * 85 + chars.index(char)
        count += 1
        if count == 5:
            data.extend((acc >> 24).to_bytes(4, "big"))
            acc, count = acc & 0xffffff, 0
    if count:
        rem = 85 * count
        data.extend((acc >> (rem - 85 * 4)).to_bytes(4, "big"))
    return bytes(data)