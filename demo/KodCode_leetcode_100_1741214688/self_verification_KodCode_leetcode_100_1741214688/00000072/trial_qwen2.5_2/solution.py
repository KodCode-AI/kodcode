def count_good_splits(binary_string: str) -> int:
    """
    Counts the number of ways to split the binary string into three non-empty substrings
    such that the bitwise XOR of the first two substrings is equal to the bitwise XOR of the last two substrings.
    """
    prefix_xor = [0]
    for char in binary_string:
        prefix_xor.append(prefix_xor[-1] ^ int(char))
    
    count = 0
    n = len(binary_string)
    for i in range(1, n-1):
        if prefix_xor[i] == prefix_xor[-1] - prefix_xor[i+1]:
            count += 1
    return count