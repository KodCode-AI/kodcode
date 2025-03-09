def longest_palindromic_substring(s: str) -> int:
    """
    Returns the length of the longest palindromic substring in s.
    """
    if not s:
        return 0

    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start, max_length = 0, 1

    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for sub-strings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    # Check for lengths greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_length = length

    return max_length