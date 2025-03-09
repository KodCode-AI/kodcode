def max_subarray_kadane(arr):
    """
    Finds the maximum sum of a contiguous subarray within a one-dimensional array of numbers.
    This implementation uses Kadane's algorithm.
    """
    max_current = max_global = arr[0]
    for num in arr[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global