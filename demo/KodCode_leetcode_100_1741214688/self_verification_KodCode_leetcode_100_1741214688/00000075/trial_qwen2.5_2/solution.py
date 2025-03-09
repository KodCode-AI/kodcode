def make_smallest_string(s: str) -> str:
    """
    Returns the lexicographically smallest string s after reversing some substrings.
    """
    s = list(s)
    for i in range(len(s)):
        start = i
        while start > 0 and s[start] < s[start - 1]:
            s[start], s[start - 1] = s[start - 1], s[start]
            start -= 1
    return ''.join(s)