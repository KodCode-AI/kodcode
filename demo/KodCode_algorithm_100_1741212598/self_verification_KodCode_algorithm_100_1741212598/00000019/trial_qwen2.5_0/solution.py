def enhanced_djb2(s, magic_constant=5381):
    """
    Returns the hash value of the given string 's' using the djb2 hash algorithm
    with a configurable magic constant.
    """
    for char in s:
        if isinstance(char, str):
            magic_constant = (magic_constant * 33) + ord(char)
        else:
            magic_constant = (magic_constant * 33) + char
    return magic_constant