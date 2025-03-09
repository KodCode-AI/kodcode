def enhanced_djb2(s, magic_constant=5381):
    """
    Returns the hash value for the input string using the djb2 hash algorithm.
    
    Args:
    s (str): The input string to be hashed.
    magic_constant (int): The magic constant used in the hash function (default is 5381).
    
    Returns:
    int: The hash value.
    """
    for char in s:
        magic_constant = ((magic_constant << 5) + magic_constant) + ord(char)  # Use ord to get ASCII value
    return magic_constant