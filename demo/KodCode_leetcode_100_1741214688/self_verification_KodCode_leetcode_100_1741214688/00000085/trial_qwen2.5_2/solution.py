def longest_balanced_substring(s: str) -> int:
    """
    Returns the length of the longest balanced substring in the given string s.
    A balanced substring has the same number of occurrences for each character.
    """
    max_len = 0
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            if all(substring.count(char) == substring.count(next(iter(substring))) for char in set(substring)):
                max_len = max(max_len, len(substring))
    return max_len