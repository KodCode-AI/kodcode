def hex_to_bin_v2(hex_val: str) -> str:
    """
    Converts a hexadecimal value (possibly with whitespace) to its binary equivalent.
    
    Raises ValueError if the input is not a valid hexadecimal number.
    """
    # Remove leading and trailing whitespace
    hex_val = hex_val.strip()
    
    # Check if the input is empty after stripping whitespace
    if not hex_val:
        raise ValueError("No value was passed to the function")
    
    # Validate if the input is a valid hexadecimal number
    valid_hex = set("0123456789abcdefABCDEF")
    if not all(char in valid_hex for char in hex_val):
        raise ValueError(f"Invalid value was passed to the function: {hex_val}")
    
    # Handle negative numbers correctly
    is_negative = hex_val.startswith('-')
    if is_negative:
        hex_val = hex_val[1:]
    
    # Convert hexadecimal to binary
    binary_val = bin(int(hex_val, 16))[2:]
    
    # Add back the negative sign if needed
    if is_negative:
        binary_val = '-' + binary_val
    
    return binary_val