def interleave_strings(first_str: str, second_str: str) -> str:
    """
    Returns a new string by interleaving characters from first_str and second_str.
    """
    result = []
    min_len = min(len(first_str), len(second_str))
    for i in range(min_len):
        result.append(first_str[i])
        result.append(second_str[i])
    result.append(first_str[min_len:])
    result.append(second_str[min_len:])
    return ''.join(result)