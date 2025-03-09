def count_palindromic_subsequences(s: str) -> int:
    """
    Returns the number of distinct palindromic subsequences in the given string s.
    The result is returned modulo 10^9 + 7.
    """
    mod = 10**9 + 7
    n = len(s)
    dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(4)]
    for i in range(n):
        dp[0][i][i] = 1  # Single character is a palindrome.
        
    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            if s[start] == s[end]:
                for j in range(1, 4):
                    dp[j][start][end] = (dp[j-1][start+1][end-1] * 2) % mod
                    if start + 1 <= end - 1:
                        dp[j][start][end] += dp[j][start+1][end-1]
                    if start + 2 <= end:
                        dp[j][start][end] += dp[j][start+2][end]
            else:
                for j in range(1, 4):
                    dp[j][start][end] = (dp[j-1][start+1][end] + dp[j-1][start][end-1]) % mod

    return (dp[3][0][n-1] - 2 + mod) % mod  # Subtract the count of palindromic subsequences that are not distinct.