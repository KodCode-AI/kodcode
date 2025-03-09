def max_subarray_sum(arr):
    """
    Finds the maximum sum of a contiguous subarray within a one-dimensional array of numbers.
    
    Args:
    arr (list of int): The input array.
    
    Returns:
    int: The maximum subarray sum.
    """
    if not arr:
        return 0
    
    max_current = max_global = arr[0]
    for num in arr[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
            
    return max_global