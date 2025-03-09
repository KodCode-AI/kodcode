def interleave_strings(first_str: str, second_str: str) -> str:
    """
    Interleave the characters from two strings and return the result.
    """
    result = []
    i, j = 0, 0
    while i < len(first_str) and j < len(second_str):
        result.append(first_str[i])
        result.append(second_str[j])
        i += 1
        j += 1
    # Append remaining characters from first_str if any
    result.extend(first_str[i:])
    # Append remaining characters from second_str if any
    result.extend(second_str[j:])
    return ''.join(result)