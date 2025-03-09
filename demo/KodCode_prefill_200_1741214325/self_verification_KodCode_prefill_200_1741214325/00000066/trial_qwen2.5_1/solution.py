def max_subarray_sum(arr):
    """
    Returns the maximum sum of a contiguous subarray within the one-dimensional array of numbers.
    """
    if not arr:
        return 0

    current_sum = max_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum