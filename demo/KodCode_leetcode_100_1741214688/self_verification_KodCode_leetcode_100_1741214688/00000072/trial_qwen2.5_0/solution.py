def count_split_ways(s):
    """
    Counts the number of ways to split the binary string s into three non-empty
    substrings such that the bitwise XOR of the first two substrings is equal to
    the bitwise XOR of the last two substrings.
    """
    n = len(s)
    if n < 6:  # At least 6 characters are needed for a valid split
        return 0
    
    prefix_xor = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_xor[i] = prefix_xor[i - 1] ^ int(s[i - 1])

    count = 0
    xor_value = prefix_xor[n]  # XOR of the entire string
    for i in range(1, n - 4):  # First split point
        for j in range(i + 1, n - 2):  # Second split point
            if prefix_xor[i] == xor_value:
                count += 1
    return count