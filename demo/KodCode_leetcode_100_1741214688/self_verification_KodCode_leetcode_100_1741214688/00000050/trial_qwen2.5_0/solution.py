def count_ways(n: int) -> int:
    """
    Returns the number of ways to represent n as a sum of consecutive positive integers.
    """
    ways = 0
    start = 1
    while start * (start + 1) < 2 * n:
        end = int((-start + (start * (start + 1) - 2 * n) ** 0.5) / 2)
        if start * (start + 1) // 2 + end * (end + 1) // 2 == n:
            ways += 1
        start += 1
    return ways