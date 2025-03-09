def remove_duplicates(s):
    """
    Returns a string with duplicate characters removed while maintaining the original order of characters.
    """
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)