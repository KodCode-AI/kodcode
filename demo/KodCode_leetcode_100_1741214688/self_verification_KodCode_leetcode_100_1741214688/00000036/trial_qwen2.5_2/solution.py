def min_flips_to_alternate(s: str) -> int:
    """
    Returns the minimum number of operations required to make the binary string 's' alternating.
    """
    len_s = len(s)
    
    # Count the number of flips to make the string start with '0' and with '1'
    flips_starting_with_0 = flips_starting_with_1 = 0
    
    for i, char in enumerate(s):
        expected_char = '0' if i % 2 == 0 else '1'
        if char != expected_char:
            flips_starting_with_0 += 1
    
    expected_char = '1' if len_s % 2 == 0 else '0'
    for i, char in enumerate(s):
        if char != expected_char:
            flips_starting_with_1 += 1
    
    # Since we count the flips for starting with '1', subtract them from the total length to get the flips for starting with '0'
    result = min(flips_starting_with_0, len_s - flips_starting_with_1)
    
    # Check if the string is already alternating
    if len_s == result:
        return result
    
    return -1 if result == len_s else result