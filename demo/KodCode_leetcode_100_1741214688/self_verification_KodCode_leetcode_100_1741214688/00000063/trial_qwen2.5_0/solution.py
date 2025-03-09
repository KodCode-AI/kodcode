def min_operations_to_k_ones(s, k):
    """
    Given a binary string s and an integer k, return the minimum number of operations
    required to make exactly k characters in the string '1'.
    """
    n = len(s)
    prefix_sum = [0]
    for char in s:
        prefix_sum.append(prefix_sum[-1] + (char == '1'))
    
    min_ops = float('inf')
    for left in range(n + 1):
        right = max(0, (k * 2 - prefix_sum[left] - (n - left)))
        ops = max(0, n - right) + left - prefix_sum[left]
        min_ops = min(min_ops, ops)
    
    return min_ops