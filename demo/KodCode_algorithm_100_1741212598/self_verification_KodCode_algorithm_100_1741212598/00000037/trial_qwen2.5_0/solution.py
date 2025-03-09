def optimized_partition(n: int) -> int:
    """
    >>> optimized_partition(1)
    1

    >>> optimized_partition(9)
    14

    >>> optimized_partition(1000000)
    55374
    """
    # Initialize a list to store the number of partitions for each value up to n
    partitions = [0] * (n + 1)
    partitions[0] = 1  # There's one way to partition 0 coins

    # Use a dynamic programming approach with nested loops to compute the partitions
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            partitions[j] += partitions[j - i]

    # Iterate until we find the smallest n where p(n) is divisible by one million
    i = 1
    while True:
        if partitions[i] % 1000000 == 0:
            return i
        i += 1