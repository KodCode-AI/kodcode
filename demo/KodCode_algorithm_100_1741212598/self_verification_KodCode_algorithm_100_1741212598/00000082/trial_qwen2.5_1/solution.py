def longest_common_subsequence(x: str, y: str) -> (int, [str]):
    """
    Returns the length of the LCS and all LCS sequences in a list of strings.
    """
    m, n = len(x), len(y)
    dp_prev = [0] * (n + 1)
    dp_curr = [0] * (n + 1)

    # Build the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp_curr[j] = dp_prev[j - 1] + 1
            else:
                dp_curr[j] = max(dp_prev[j], dp_curr[j - 1])

        # Swap the DP arrays
        dp_prev, dp_curr = dp_curr, dp_prev

    # Reconstruct all LCS sequences
    lcs_length = dp_prev[-1]
    sequences = set()

    def backtrack(i, j, seq):
        if i == 0 or j == 0:
            sequences.add(''.join(seq)[::-1])
            return
        if x[i - 1] == y[j - 1]:
            seq.append(x[i - 1])
            backtrack(i - 1, j - 1, seq)
            seq.pop()
        elif dp_prev[j - 1] > dp_prev[j]:
            backtrack(i, j - 1, seq)
        else:
            backtrack(i - 1, j, seq)

    backtrack(m, n, [])
    return lcs_length, list(sequences)