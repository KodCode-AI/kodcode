def bin_to_octal(bin_string: str) -> str:
    """
    Converts a binary string to its octal equivalent.
    """
    if not all(c in '01' for c in bin_string):
        raise ValueError("Non-binary value was passed to the function")
    if not bin_string:  # Handle empty string
        return ""
    
    # Group binary string into chunks of 3, padding with leading zeros if necessary
    padded_bin = bin_string.zfill((len(bin_string) + 2) // 3 * 3)
    octal = ""
    for i in range(0, len(padded_bin), 3):
        chunk = padded_bin[i:i+3]
        octal_digit = int(chunk, 2)
        octal += str(octal_digit)
    
    return octal