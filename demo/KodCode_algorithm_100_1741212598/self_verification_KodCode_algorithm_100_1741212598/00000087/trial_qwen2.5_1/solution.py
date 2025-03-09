def bin_to_octal(bin_string: str) -> str:
    """
    Converts a binary string to its octal equivalent.
    """
    if not all(c in '01' for c in bin_string):
        raise ValueError("Non-binary value was passed to the function")
    
    octal_string = ''
    groups = [bin_string[i:i+3] for i in range(0, len(bin_string), 3)]
    for group in groups:
        group += '0' * (3 - len(group))  # Pad with zeros if necessary
        octal_digit = int(group, 2)
        octal_string += str(octal_digit)
    return octal_string.lstrip('0') or '0'  # Remove leading zeros, return '0' if empty