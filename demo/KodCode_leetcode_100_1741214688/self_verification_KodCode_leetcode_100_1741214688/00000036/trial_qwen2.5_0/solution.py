def min_operations_to_alternate(s: str) -> int:
    """
    Returns the minimum number of operations required to make the binary string alternating.
    If it's impossible, return -1.
    """
    n = len(s)
    # Count the number of mismatches if starting with '0' and '1'
    count_0 = sum(s[i] != '0' for i in range(n))
    count_1 = sum(s[i] != '1' for i in range(n))
    
    # The minimum operations is the minimum of the two counts, but not more than n//2
    min_ops = min(count_0, count_1)
    if min_ops > n // 2:
        return -1
    return min_ops