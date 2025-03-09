def minimum_cost(nums, costs):
    """
    Returns the minimum cost to set all elements in nums to 0.
    """
    total_cost = 0
    min_cost = min(costs)  # Find the minimum cost in the costs list
    
    for i in range(len(nums)):
        if nums[i] != 0:
            total_cost += min_cost  # Use the minimum cost to set nums[i] to 0
    
    return total_cost