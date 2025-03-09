def count_reversible_numbers(max_power: int) -> int:
    """
    Returns the number of reversible numbers below 10^max_power.
    """
    if max_power == 1:
        return 5  # There are 5 reversible numbers below 10: 1, 2, 3, 4, 5

    # Precompute the count for smaller powers of 10
    counts = [0] * (max_power + 1)
    counts[1] = 5
    for i in range(2, max_power + 1):
        if i % 2 == 0:
            # For even powers of 10, the count is 5 * 5 * 5 * 2
            half_power = i // 2
            counts[i] = 5 * 5 * 5 * 2
        else:
            # For odd powers of 10, the count is 5 * 5 * 5 * 5
            half_power = (i - 1) // 2
            counts[i] = 5 * 5 * 5 * 5

    return counts[max_power]