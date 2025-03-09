def max_subarray_sum(arr):
    """
    Returns the maximum sum of a contiguous subarray within the given array.
    The subarray must contain at least one number.
    """
    if not arr:
        raise ValueError("Array cannot be empty")
        
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum