def max_length_without_010(s: str) -> int:
    """
    Returns the maximum length of the string s such that it does not contain the substring "010".
    """
    dp = [1] * 3
    for c in s:
        if c == '0':
            dp[0], dp[1] = max(dp[1], dp[2]), dp[0] + 1
        else:
            dp[0], dp[1] = max(dp[0], dp[2]), dp[1] + 1
        dp[2] = max(dp[0], dp[1], dp[2])
    return dp[2]