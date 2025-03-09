def count_distinct_palindromic_subsequences(s):
    """
    Given a string s, return the number of distinct palindromic subsequences modulo 10^9 + 7.
    """
    MOD = 10**9 + 7
    n = len(s)
    first_occurrence = {}
    last_occurrence = {}
    dp = [[0] * n for _ in range(n)]
    distinct_subsequences = 0
    
    # Initialize the DP table and first/last occurrences
    for i in range(n):
        first_occurrence[s[i]] = first_occurrence.get(s[i], []) + [i]
        last_occurrence[s[i]] = last_occurrence.get(s[i], []) + [i]
    
    for i in range(n):
        dp[i][i] = 1  # Single character is always a palindrome
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = (dp[i + 1][j - 1] + 2) % MOD
                for k in range(1, len(first_occurrence[s[i]])):
                    if first_occurrence[s[i]][k] <= j and last_occurrence[s[i]][-k - 1] >= i + 1:
                        dp[i][j] -= dp[first_occurrence[s[i]][k] + 1][last_occurrence[s[i]][-k - 1] - 1]
                        dp[i][j] %= MOD
            else:
                dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % MOD
    
    # Sum up all subsequences that start and end with the same character to avoid double counting
    for i in range(n):
        distinct_subsequences += dp[i][i]
        distinct_subsequences %= MOD
    
    # Sum up all subsequences of the form s[i:j] where s[i] == s[j]
    for i in range(n):
        for j in range(n):
            if s[i] == s[j]:
                distinct_subsequences += dp[i][j]
                distinct_subsequences %= MOD
    
    return distinct_subsequences