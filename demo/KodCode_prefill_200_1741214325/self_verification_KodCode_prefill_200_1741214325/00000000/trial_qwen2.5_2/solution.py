def remove_duplicates(input_string: str) -> str:
    """
    Returns a new string with duplicate characters removed while preserving the original order.
    """
    seen = set()
    result = []
    for char in input_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)