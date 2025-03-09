def find_min_difference(numbers: list[int]) -> int:
    """
    Find the minimum possible difference between the sums of two subsets of the given list of integers.
    """
    total_sum = sum(numbers)
    n = len(numbers)
    dp = [[0] * (total_sum // 2 + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, total_sum // 2 + 1):
            if numbers[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], numbers[i - 1] + dp[i - 1][j - numbers[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]
    
    closest_sum = dp[n][total_sum // 2]
    return total_sum - 2 * closest_sum