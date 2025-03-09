def hex_to_bin_optimized(hex_num: str) -> str:
    """
    Convert a hexadecimal value to its binary equivalent, optimized for performance.
    """
    if not hex_num.strip():
        raise ValueError("No value was passed to the function")
    
    if hex_num[0] == '-':
        binary_result = '-'
        hex_num = hex_num[1:]
    else:
        binary_result = ''
    
    hex_to_bin_map = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    
    hex_num = hex_num.strip().upper()
    
    for char in hex_num:
        if char in hex_to_bin_map:
            binary_result += hex_to_bin_map[char]
        else:
            raise ValueError("Invalid value was passed to the function")
    
    return binary_result