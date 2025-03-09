def min_cost_to_set(nums, costs):
    """
    Returns the minimum cost to set all elements in nums to 0.
    """
    min_cost = float('inf')
    for i in range(len(nums)):
        current_cost = sum(costs[j] for j in range(len(nums)) if nums[j] == nums[i])
        min_cost = min(min_cost, current_cost)
    return min_cost