def min_operations_to_k_ones(binary_str, k):
    """
    Calculates the minimum number of operations required to have exactly k '1's in the binary string.
    """
    ones = sum(1 for char in binary_str if char == '1')
    if ones == k:
        return 0
    
    max_consecutive_ones = current_consecutive_ones = binary_str.count('1')
    for i in range(len(binary_str)):
        if binary_str[i] == '1':
            current_consecutive_ones -= 1
        else:
            max_consecutive_ones = max(max_consecutive_ones, (i + 1 - current_consecutive_ones) - 1)
            current_consecutive_ones = 0
    
    operations = k - ones if binary_str[-1] == '0' else k - ones + max_consecutive_ones
    return operations