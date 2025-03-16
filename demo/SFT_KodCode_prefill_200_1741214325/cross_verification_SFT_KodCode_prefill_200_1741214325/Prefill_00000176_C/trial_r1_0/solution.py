def min_deletions_to_palindrome(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0
    
    # Create a 2D DP table to store lengths of the longest palindromic subsequence
    dp = [[0] * n for _ in range(n)]
    
    # Fill the DP table in a bottom-up manner
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j:
                dp[i][j] = 1
            else:
                if s[i] == s[j]:
                    if j == i + 1:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    
    # The length of the longest palindromic subsequence
    lps_length = dp[0][n - 1]
    return len(s) - lps_length