def hex_to_bin_v2(hex_val):
    """
    Convert a hexadecimal value to its binary equivalent.
    
    Args:
    hex_val (str): A string representing a hexadecimal number (optionally with leading/trailing whitespace).
    
    Returns:
    str: A string representing the binary equivalent of the input hexadecimal number.
    
    Raises:
    ValueError: If the input string contains invalid characters or is not a valid hexadecimal number.
    """
    # Strip leading and trailing whitespace
    hex_val = hex_val.strip()
    
    # Check if the input string is empty
    if not hex_val:
        raise ValueError("No value was passed to the function")
    
    # Check for invalid characters
    if not all(c in '0123456789abcdefABCDEF' for c in hex_val):
        raise ValueError("Invalid value was passed to the function")
    
    return bin(int(hex_val, 16))[2:]