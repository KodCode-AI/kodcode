def max_length_no_010(s: str) -> int:
    """
    Returns the maximum length of the string s (consisting only of '0's and '1's) 
    such that it does not contain the substring "010" after performing any number 
    of adjacent flips.
    """
    n = len(s)
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    dp = [[0, 0] for _ in range(n+1)]
    dp[0] = [0, 0]  # No flips, No 010
    dp[1] = [1, 0 if s[0] == '1' else 1]  # One flip, No 010
    
    for i in range(2, n+1):
        dp[i][0] = dp[i-1][0] + 1  # No flip, use the previous configuration
        if s[i-1] == '0':
            dp[i][1] = dp[i-1][0] + 1  # Flip, use the previous no 010
        else:
            dp[i][1] = dp[i-1][1] + 1  # No flip, use the previous flip
        if i >= 3 and s[i-1] == '1' and s[i-2] == '0' and s[i-3] == '0':
            dp[i][1] = max(dp[i][1], dp[i-3][0] + 1)  # Check for "010" pattern
    
    return max(dp[n])