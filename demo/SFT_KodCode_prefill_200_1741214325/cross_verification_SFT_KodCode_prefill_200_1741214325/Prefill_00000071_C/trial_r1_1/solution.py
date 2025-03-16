def sum_of_multiples() -> int:
    limit = 1000
    n = limit - 1  # Since we consider numbers below 1000

    # Calculate sum for multiples of 3
    k3 = n // 3
    sum3 = 3 * (k3 * (k3 + 1)) // 2

    # Calculate sum for multiples of 5
    k5 = n // 5
    sum5 = 5 * (k5 * (k5 + 1)) // 2

    # Calculate sum for multiples of 15 to avoid double-counting
    k15 = n // 15
    sum15 = 15 * (k15 * (k15 + 1)) // 2

    # Apply inclusion-exclusion principle
    total = sum3 + sum5 - sum15
    return total