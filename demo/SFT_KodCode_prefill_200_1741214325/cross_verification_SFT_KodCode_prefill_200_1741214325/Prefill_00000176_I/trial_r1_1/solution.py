def min_deletions_to_palindrome(s):
    n = len(s)
    if n == 0:
        return 0

    # Create a 2D DP table initialized to 0
    dp = [[0] * n for _ in range(n)]

    # Fill the table for substrings of length 1
    for i in range(n):
        dp[i][i] = 1

    # Fill the table for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = 2
        else:
            dp[i][i + 1] = 1

    # Fill the table for substrings of lengths from 3 to n
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = 2 + (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The length of the longest palindromic subsequence
    lps_length = dp[0][n - 1]
    return n - lps_length