def min_deletions_to_palindrome(s: str) -> int:
    """
    Returns the minimum number of deletions required to make a string a palindrome.
    """
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    # Fill dp table
    for gap in range(1, n):
        for i in range(n - gap):
            j = i + gap
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i + 1][j]) + 1
                
    return dp[0][n - 1]