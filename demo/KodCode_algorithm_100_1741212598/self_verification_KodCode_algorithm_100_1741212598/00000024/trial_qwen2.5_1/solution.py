def hex_to_bin_optimized(hex_num: str) -> str:
    """
    Convert a hexadecimal value to its binary equivalent, optimized for performance.
    >>> hex_to_bin_optimized("AC")
    "10101100"
    >>> hex_to_bin_optimized("9A4")
    "100110100100"
    >>> hex_to_bin_optimized("   12f   ")
    "100101111"
    >>> hex_to_bin_optimized("FfFf")
    "1111111111111111"
    >>> hex_to_bin_optimized("-fFfF")
    "-1111111111111111"
    >>> hex_to_bin_optimized("F-f")
    Traceback (most recent call last):
        ...
    ValueError: Invalid value was passed to the function
    >>> hex_to_bin_optimized("")
    Traceback (most recent call last):
        ...
    ValueError: No value was passed to the function
    """
    hex_num = hex_num.strip().lstrip('-')
    if not hex_num or not all(c in '0123456789abcdefABCDEF' for c in hex_num):
        raise ValueError("Invalid value was passed to the function")
    
    # Map hex digits to their binary representations
    hex_to_bin = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    
    # Convert to binary
    bin_num = ''.join(hex_to_bin[c] for c in hex_num)
    if hex_num.startswith('-'):
        bin_num = '-' + bin_num
    
    return bin_num