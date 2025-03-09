def count_distinct_palindromic_subsequences(s: str) -> int:
    """
    Returns the number of distinct palindromic subsequences of the string `s`.
    The result is returned modulo 10^9 + 7.
    """
    MOD = 10**9 + 7
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n-1, -1, -1):
        dp[i][i] = 1  # Single character is always a palindrome
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = (2 * dp[i+1][j-1]) % MOD
                k = j - 1
                while k > i:
                    if s[i] == s[k]:
                        dp[i][j] += (dp[i+1][k-1] - dp[i+1][j-1] + MOD) % MOD
                        break
                    k -= 1
            else:
                dp[i][j] = (dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1] + MOD) % MOD

    return (dp[0][n-1] - 1 + MOD) % MOD  # Subtract 1 to exclude the empty subsequence