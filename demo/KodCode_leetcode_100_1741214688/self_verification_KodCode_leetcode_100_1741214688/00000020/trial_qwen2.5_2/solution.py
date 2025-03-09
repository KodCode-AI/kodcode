def max_length(s):
    """
    Returns the maximum length of a binary string s after performing the specified operation
    such that the string does not contain the substring "010".
    """
    dp = [[[0, 0, 0] for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]
    for i in range(len(s), -1, -1):
        for j in range(len(s), -1, -1):
            if i == len(s):
                if j == len(s):
                    dp[i][j][0] = 0
                    dp[i][j][1] = 0
                    dp[i][j][2] = 0
                elif s[i] == '0':
                    dp[i][j][1] = 1 + dp[i + 1][j][1] + dp[i + 1][j][2]
                    dp[i][j][2] = dp[i + 1][j][2]
                else:
                    dp[i][j][1] = 1 + dp[i + 1][j][1]
                    dp[i][j][2] = 1 + dp[i + 1][j][2]
            elif j == len(s):
                if s[i] == '0':
                    dp[i][j][1] = 1 + dp[i][j + 1][1] + dp[i][j + 1][0]
                    dp[i][j][2] = 1 + dp[i][j + 1][0] + dp[i][j + 1][2]
                else:
                    dp[i][j][0] = 1 + dp[i][j + 1][0] + dp[i][j + 1][1]
                    dp[i][j][1] = 1 + dp[i][j + 1][1]
                    dp[i][j][2] = 1 + dp[i][j + 1][2]
            else:
                if s[i] == '0':
                    dp[i][j][1] = 1 + dp[i + 1][j][1] + dp[i + 1][j][2]
                    dp[i][j][2] = dp[i + 1][j][2]
                else:
                    dp[i][j][1] = 1 + dp[i + 1][j][1]
                    dp[i][j][2] = 1 + dp[i + 1][j][2]
    return max(dp[0][0])