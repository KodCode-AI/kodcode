def min_deletions_to_palindrome(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0
    # Initialize a DP table where dp[i][j] represents the length of the longest
    # palindromic subsequence from index i to j.
    dp = [[0] * n for _ in range(n)]
    
    # All substrings of length 1 are palindromes.
    for i in range(n):
        dp[i][i] = 1
    
    # Fill the table for substrings of length >= 2.
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if s[i] == s[j]:
                if l == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    
    # The length of the longest palindromic subsequence is dp[0][n-1].
    lps_length = dp[0][n - 1]
    return n - lps_length