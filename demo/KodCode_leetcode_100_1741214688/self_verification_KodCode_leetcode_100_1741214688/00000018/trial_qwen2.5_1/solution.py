def min_cost(nums, costs):
    """
    Returns the minimum cost to set all elements in nums to 0.
    """
    max_num = max(nums)
    return sum(costs[i] for i in range(len(nums)) if nums[i] == max_num)