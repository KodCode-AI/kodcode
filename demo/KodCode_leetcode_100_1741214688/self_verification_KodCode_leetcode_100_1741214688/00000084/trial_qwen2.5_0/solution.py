def max_monotonic_group(heights):
    """
    Finds the maximum size of a monotonic group in the list of building heights.
    """
    max_len = 1
    current_len = 1

    for i in range(1, len(heights)):
        if heights[i] - heights[i-1] == 1 or heights[i] - heights[i-1] == -1:
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 1

    return max_len