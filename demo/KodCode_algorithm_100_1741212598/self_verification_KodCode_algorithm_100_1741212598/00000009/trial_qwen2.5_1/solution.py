def find_min_difference(numbers: list[int]) -> int:
    """
    Returns the minimum possible difference between the sums of the two subsets.
    """
    total_sum = sum(numbers)
    n = len(numbers)
    dp = [[False] * (total_sum + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(1, total_sum + 1):
            if numbers[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - numbers[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    
    for j in range(total_sum // 2, -1, -1):
        if dp[n][j]:
            subset_sum = j
            break
    
    return total_sum - 2 * subset_sum