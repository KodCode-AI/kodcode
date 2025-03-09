def max_subarray_sum(arr):
    """
    Returns the maximum sum of a contiguous subarray within the given array.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    int: Maximum sum of a contiguous subarray.
    """
    if not arr:
        raise ValueError("Array is empty")
    
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum