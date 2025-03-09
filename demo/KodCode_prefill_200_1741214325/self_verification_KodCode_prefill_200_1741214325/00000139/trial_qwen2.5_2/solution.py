def max_subarray_kadane(arr):
    """
    Find the maximum sum of a subarray within the given array using Kadane's algorithm.
    """
    max_current = max_global = arr[0]
    for num in arr[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global