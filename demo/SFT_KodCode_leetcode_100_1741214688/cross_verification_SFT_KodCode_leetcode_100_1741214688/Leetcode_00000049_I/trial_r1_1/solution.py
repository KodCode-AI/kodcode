def shortest_subarray_with_sum_at_least_target(nums, target):
    n = len(nums)
    if n < 2:
        return 0
    min_len = float('inf')
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if j > i:
                if current_sum >= target:
                    current_length = j - i + 1
                    if current_length < min_len:
                        min_len = current_length
                    break  # no need to check further for this i
    return min_len if min_len != float('inf') else 0