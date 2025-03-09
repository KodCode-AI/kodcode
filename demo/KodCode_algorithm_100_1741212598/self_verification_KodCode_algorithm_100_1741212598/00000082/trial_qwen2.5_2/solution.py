def longest_common_subsequence(x, y):
    """
    Returns the length of the LCS and all possible LCS sequences as a list of strings.
    """
    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(2)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + 1
            else:
                dp[i % 2][j] = max(dp[(i - 1) % 2][j], dp[i % 2][j - 1])
    
    lcs_length = dp[m % 2][n]
    lcs_sequences = set()
    i, j = m, n
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            lcs_sequences.add(x[i - 1])
            i -= 1
            j -= 1
        elif dp[i % 2][j - 1] > dp[(i - 1) % 2][j]:
            j -= 1
        else:
            i -= 1
    
    lcs_strs = [""] * lcs_length
    lcs_sequences = list(lcs_sequences)
    backtrack(i, j, lcs_strs, lcs_sequences, x, y, lcs_length)
    
    for seq in lcs_sequences:
        print(f"len = {lcs_length}, sub-sequence = {seq}")
    
    return lcs_length, lcs_sequences

def backtrack(i, j, lcs_strs, lcs_sequences, x, y, lcs_length):
    if i == 0 or j == 0:
        lcs_sequences.append(''.join(reversed(lcs_strs)))
        return
    
    if x[i - 1] == y[j - 1]:
        lcs_strs[lcs_length - 1] = x[i - 1]
        backtrack(i - 1, j - 1, lcs_strs, lcs_sequences, x, y, lcs_length - 1)
    else:
        backtrack(i, j - 1, lcs_strs, lcs_sequences, x, y, lcs_length)
        backtrack(i - 1, j, lcs_strs, lcs_sequences, x, y, lcs_length)