def optimized_partition(n: int) -> int:
    """
    >>> optimized_partition(1)
    1

    >>> optimized_partition(9)
    14

    >>> optimized_partition(1000000)
    55374
    """
    partition = [0] * (n + 1)
    partition[0] = 1  # There's 1 way to partition 0, the empty partition.
    
    for i in range(1, n + 1):
        for k in range(i, n + 1):
            partition[k] += partition[k - i]
    
    for i in range(1, n + 1):
        if partition[i] % 1000000 == 0:
            return i

    return -1  # This line should never be reached for n in the given range.