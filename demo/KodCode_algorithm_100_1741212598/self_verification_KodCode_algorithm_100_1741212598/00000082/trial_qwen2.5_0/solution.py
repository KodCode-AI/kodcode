def longest_common_subsequence(x, y):
    """
    Returns the length of the LCS and all possible LCS sequences.
    """
    m, n = len(x), len(y)
    dp = [[""] * (n + 1) for _ in range(2)]
    dp[0] = [[0] * (n + 1), [c for c in y if c == x[0]]]  # Initialize the first row

    # Fill the DP table
    for i in range(1, m):
        for j in range(1, n + 1):
            if x[i] == y[j - 1]:
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + x[i]
            else:
                if len(dp[(i - 1) % 2][j]) > len(dp[i % 2][j - 1]):
                    dp[i % 2][j] = dp[(i - 1) % 2][j]
                elif len(dp[(i - 1) % 2][j]) < len(dp[i % 2][j - 1]):
                    dp[i % 2][j] = dp[i % 2][j - 1]
                else:
                    dp[i % 2][j] = dp[(i - 1) % 2][j] + dp[i % 2][j - 1]

    # Gather all LCS sequences
    lcs_sequences = []
    current_sequences = [dp[(m - 1) % 2][n]]
    for seq in current_sequences:
        if seq in dp[(m - 1) % 2]:
            lcs_sequences.append(seq)
    
    return len(dp[(m - 1) % 2][n]), lcs_sequences

def print_lcs_sequences(x, y):
    lcs_length, lcs_sequences = longest_common_subsequence(x, y)
    print(f"len = {lcs_length}, sub-sequence = {lcs_sequences[0]}")
    for seq in lcs_sequences[1:]:
        print(f"len = {lcs_length}, sub-sequence = {seq}")

a = "AGGTAB"
b = "GXTXAYB"
print_lcs_sequences(a, b)
# Output:
# len = 4, sub-sequence = GTAB
# len = 4, sub-sequence = GBAB
# (4, ['GTAB', 'GBAB'])