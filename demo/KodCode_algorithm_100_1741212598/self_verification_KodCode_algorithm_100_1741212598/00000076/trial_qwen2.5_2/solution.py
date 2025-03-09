def hex_to_bin_v2(hex_val):
    """
    Converts a hexadecimal value to its binary equivalent.
    
    :param hex_val: A string representing a hexadecimal number (optional whitespace).
    :return: A string representing the binary equivalent of the input hexadecimal number.
    :raises ValueError: If the input string is invalid or empty.
    """
    # Strip leading and trailing whitespace
    hex_val = hex_val.strip()
    
    # Validate the input
    if not hex_val or not set(hex_val).issubset(set('0123456789abcdefABCDEF')):
        raise ValueError("Invalid value was passed to the function")
    
    # Handle negative numbers
    negative = hex_val.startswith('-')
    if negative:
        hex_val = hex_val[1:]
    
    # Convert hexadecimal to binary
    bin_val = bin(int(hex_val, 16))[2:]
    
    # Add sign back if necessary
    if negative:
        bin_val = '-' + bin_val
    
    return bin_val