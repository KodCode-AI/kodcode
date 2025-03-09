def smallest_string(s: str) -> str:
    """
    Returns the lexicographically smallest string that can be obtained by replacing
    any two adjacent characters with the lexicographically smallest character among them.
    """
    s = list(s)  # Convert string to list for in-place modification
    i = 0
    n = len(s)
    while i < n - 1:
        if s[i] <= s[i + 1]:
            i += 1
        else:
            s[i] = s[i + 1]  # Replace the character
            n -= 1  # Reduce the length since one character is effectively removed
    return ''.join(s)