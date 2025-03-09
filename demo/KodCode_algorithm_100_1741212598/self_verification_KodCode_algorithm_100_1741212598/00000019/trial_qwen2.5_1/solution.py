def enhanced_djb2(s: str, magic_constant: int = 5381) -> int:
    """
    Returns the hash value of the string using the djb2 hash algorithm with a configurable magic constant.
    """
    for char in s:
        magic_constant = ((magic_constant * 33) + ord(char)) % 0xFFFFFFFF
    return magic_constant