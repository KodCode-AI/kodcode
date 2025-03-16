def bin_to_octal(bin_string: str) -> str:
    """
    Converts a binary string to its octal equivalent.
    """
    if not bin_string:
        return ''
    for c in bin_string:
        if c not in {'0', '1'}:
            raise ValueError("Non-binary value was passed to the function")
    n = int(bin_string, 2)
    return f"{n:o}"