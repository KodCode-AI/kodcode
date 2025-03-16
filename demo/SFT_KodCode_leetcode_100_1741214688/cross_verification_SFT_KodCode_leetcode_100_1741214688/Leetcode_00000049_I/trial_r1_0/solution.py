def shortest_subarray_with_sum_at_least_target(nums, target):
    n = len(nums)
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + nums[i]
    
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            if s[i + l] - s[i] >= target:
                return l
    return 0