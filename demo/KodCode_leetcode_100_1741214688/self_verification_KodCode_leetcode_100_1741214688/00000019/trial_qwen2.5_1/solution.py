def smallest_substring(s: str) -> str:
    """
    Returns the lexicographically smallest substring that can be formed by rearranging any number of characters within the string.
    """
    if len(s) <= 1:
        return s
    # Convert string to list for mutations
    chars = list(s)
    n = len(chars)
    # Sort the string to find the smallest character
    min_char = min(chars)
    start = None
    # Find starting index of the smallest character
    for i in range(n):
        if chars[i] == min_char:
            start = i
            break
    # Find the ending index of the smallest character
    for i in range(start, n):
        if chars[i] > min_char:
            end = i
            break
    else:
        end = n
    # Form the smallest substring by taking all characters from the sorted string up to the first occurrence of min_char
    smallest_sub = ''.join(sorted(s[:end]))
    return smallest_sub