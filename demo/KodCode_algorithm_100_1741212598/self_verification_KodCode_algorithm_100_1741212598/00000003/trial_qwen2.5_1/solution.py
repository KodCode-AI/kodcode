def interleave_strings(first_str: str, second_str: str) -> str:
    """
    Interleaves two strings and returns the result.
    If one string is longer, the extra characters are appended to the end.
    """
    result = []
    i, j = 0, 0
    len1, len2 = len(first_str), len(second_str)
    
    while i < len1 and j < len2:
        result.append(first_str[i])
        result.append(second_str[j])
        i += 1
        j += 1
    
    # Append any remaining characters from the longer string
    result.append(first_str[i:])
    result.append(second_str[j:])
    
    return ''.join(result)