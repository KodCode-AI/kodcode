def max_monotonic_group(heights):
    """
    Returns the maximum size of a monotonic group of buildings with consecutive heights.

    :param heights: List[int] representing the heights of buildings.
    :return: int representing the maximum size of such a monotonic group.
    """
    n = len(heights)
    max_length = 1
    current_length = 1

    for i in range(1, n):
        if heights[i] == heights[i - 1] + 1 or heights[i] == heights[i - 1] - 1:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1

    return max_length