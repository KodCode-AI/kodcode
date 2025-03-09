To find the largest rectangle in a histogram, we can use a stack-based approach. The idea is to maintain a stack of indices of the histogram bars, ensuring that the heights of the bars are in non-decreasing order. While iterating through the histogram, if we encounter a bar that is shorter than the bar at the index on top of the stack, it means we can calculate the area of a rectangle with the top bar as the shortest bar. We then pop the stack, calculate the area, and update the maximum area if needed. This process continues until we have processed all the bars.

def largest_rectangle_in_histogram(heights):
    """
    Finds the largest rectangle in a histogram.
    Args:
    heights: A list of integers representing the heights of the histogram bars.

    Returns:
    The area of the largest rectangle in the histogram.
    """
    if not heights:
        return 0

    stack = [-1]  # Initialize the stack with a sentinel value -1
    max_area = 0

    for i, h in enumerate(heights):
        # Pop from stack until the current bar is not taller than the bar at the
        # index on top of the stack
        while stack[-1] != -1 and heights[stack[-1]] >= h:
            height = heights[stack.pop()]
            # Compute the width of the rectangle with the popped height
            width = i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    # Process the remaining bars in the stack
    while stack[-1] != -1:
        height = heights[stack.pop()]
        width = len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area