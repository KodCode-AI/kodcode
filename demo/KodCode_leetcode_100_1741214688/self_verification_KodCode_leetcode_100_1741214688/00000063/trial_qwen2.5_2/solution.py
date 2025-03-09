def min_operations_to_k_ones(s: str, k: int) -> int:
    """
    Returns the minimum number of operations required to make exactly k characters in the string '1'.
    """
    n = len(s)
    left_ones = s.count('1', 0, k)
    min_ops = left_ones

    for right in range(k, n):
        left_ones += s[right] == '1'
        left_ones -= s[right - k] == '1'
        min_ops = min(min_ops, left_ones)
    
    return min_ops