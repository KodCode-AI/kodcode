def hex_to_bin_optimized(hex_num: str) -> str:
    """
    Convert a hexadecimal value to its binary equivalent, optimized for performance.
    """
    # Remove leading/trailing whitespace
    hex_num = hex_num.strip()
    
    # Check for negative numbers
    if hex_num.startswith('-'):
        hex_num = hex_num[1:]
        bin_out = '-'
    else:
        bin_out = ''
    
    # Hex to Bin Conversion
    hex_to_bin_map = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    
    for char in hex_num.upper():
        if char in hex_to_bin_map:
            bin_out += hex_to_bin_map[char]
        else:
            raise ValueError("Invalid value was passed to the function")
    
    return bin_out