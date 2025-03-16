def bin_to_octal(bin_string: str) -> str:
    """
    Converts a binary string to its octal equivalent.
    """
    if not bin_string:
        return ''
    for char in bin_string:
        if char not in ('0', '1'):
            raise ValueError("Non-binary value was passed to the function")
    decimal = int(bin_string, 2)
    octal = oct(decimal)
    return octal[2:]