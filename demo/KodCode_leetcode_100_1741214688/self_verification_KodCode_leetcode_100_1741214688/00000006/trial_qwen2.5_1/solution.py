def smallest_by_reversing_substrings(s: str) -> str:
    """
    Returns the lexicographically smallest string by reversing substrings any number of times.
    """
    n = len(s)
    result = s
    
    for start in range(n):
        for end in range(start + 1, n + 1):
            substr = s[start:end]
            reversed_substr = substr[::-1]
            new_str = s[:start] + reversed_substr + s[end:]
            if new_str < result:
                result = new_str
    
    return result