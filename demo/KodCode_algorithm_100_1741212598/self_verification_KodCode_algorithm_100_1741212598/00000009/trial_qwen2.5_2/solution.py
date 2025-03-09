def find_min_difference(numbers: list[int]) -> int:
    """
    Returns the minimum possible difference between the sums of two subsets.
    """
    total_sum = sum(numbers)
    n = len(numbers)
    dp = [[False] * (total_sum + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(total_sum + 1):
            if dp[i - 1][j]:
                dp[i][j] = True
            elif j >= numbers[i - 1]:
                dp[i][j] = dp[i - 1][j - numbers[i - 1]]

    target = total_sum // 2
    while target >= 0 and not dp[n][target]:
        target -= 1

    return total_sum - 2 * target