def longest_common_subsequence(text1: str, text2: str, mask: str) -> str:
    """
    Finds the longest common subsequence (LCS) between text1 and text2 and then modifies it based on the mask.
    """
    m, n = len(text1), len(text2)
    dp = [["" for _ in range(n + 1)] for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1] and mask[i - 1] == '1':
                dp[i][j] = dp[i - 1][j - 1] + text1[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)
    
    return max(dp[-1], key=len)

# Example usage:
# text1 = "abcde"
# text2 = "ace"
# mask = "10101"
# result = longest_common_subsequence(text1, text2, mask)  # result should be "ace"