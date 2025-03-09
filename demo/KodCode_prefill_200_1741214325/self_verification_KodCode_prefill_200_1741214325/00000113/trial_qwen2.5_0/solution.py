def largest_rectangle_in_histogram(histogram):
    """
    Finds the largest rectangle that can be formed in a histogram with the given heights.
    :param histogram: A list of non-negative integers representing the heights of the bars.
    :return: The area of the largest rectangle.
    """
    stack = []
    max_area = 0
    index = 0
    while index < len(histogram):
        if not stack or histogram[stack[-1]] <= histogram[index]:
            stack.append(index)
            index += 1
        else:
            top_of_stack = stack.pop()
            height = histogram[top_of_stack]
            width = index if not stack else index - stack[-1] - 1
            max_area = max(max_area, height * width)
    while stack:
        top_of_stack = stack.pop()
        height = histogram[top_of_stack]
        width = index if not stack else len(histogram) - stack[-1] - 1
        max_area = max(max_area, height * width)
    return max_area