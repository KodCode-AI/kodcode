def min_deletions_to_palindrome(s):
    n = len(s)
    if n == 0:
        return 0

    # Create a DP table with n x n size initialized to 0
    dp = [[0] * n for _ in range(n)]

    # Fill the diagonal (substrings of length 1)
    for i in range(n):
        dp[i][i] = 1

    # Fill the DP table for substrings of length > 1
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                if j == i + 1:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The length of the longest palindromic subsequence
    lps_length = dp[0][n - 1]
    return n - lps_length