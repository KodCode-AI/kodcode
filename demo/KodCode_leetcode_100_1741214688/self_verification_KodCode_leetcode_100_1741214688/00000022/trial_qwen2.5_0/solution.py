def longest_palindrome_length(s: str) -> int:
    """
    Returns the length of the longest palindromic substring in the given string s.
    """
    if not s:
        return 0

    n = len(s)
    dp = [[False] * n for _ in range(n)]
    maxLength = 1

    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for substrings of length 2
    start = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            maxLength = 2
            start = i

    # Check for lengths greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > maxLength:
                    maxLength = length
                    start = i

    return maxLength