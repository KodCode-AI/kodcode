def max_monotonic_group_size(heights):
    """
    Returns the maximum size of a monotonic group of buildings.
    """
    max_size = 1  # At least one building can be a group.
    current_size = 1  # Start with the first building in the group.
    
    # Iterate through the heights to find the longest monotonic sequence.
    for i in range(1, len(heights)):
        if heights[i] == heights[i-1] + 1 or heights[i] == heights[i-1] - 1:
            current_size += 1
            max_size = max(max_size, current_size)
        else:
            current_size = 1  # Reset the count if the sequence is broken.
    
    return max_size