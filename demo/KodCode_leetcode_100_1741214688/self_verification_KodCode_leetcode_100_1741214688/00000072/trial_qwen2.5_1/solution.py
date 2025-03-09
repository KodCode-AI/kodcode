def count_split_ways(s):
    """
    Counts the number of ways to split the binary string s into three non-empty substrings
    such that the bitwise XOR of the first two substrings is equal to the bitwise XOR of the
    last two substrings.
    """
    total_xor = sum(int(char) for char in s)
    prefix_xor = [0]
    
    for char in s:
        prefix_xor.append(prefix_xor[-1] ^ int(char))
    
    count = 0
    for i in range(1, len(prefix_xor) - 1):
        if prefix_xor[i] == prefix_xor[-1] - prefix_xor[i]:
            count += 1
    
    return count