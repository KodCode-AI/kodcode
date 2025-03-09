def max_subarray_sum(arr):
    """
    Returns the maximum sum of a contiguous subarray within the one-dimensional array of numbers.
    """
    if not arr:
        return 0
    
    # Initialize max_sum and current_sum with the first element
    max_sum = current_sum = arr[0]
    
    # Iterate through the array starting from the second element
    for num in arr[1:]:
        # If current_sum is negative, discard it and start a new subarray
        current_sum = max(num, current_sum + num)
        # Update max_sum if current_sum is greater
        max_sum = max(max_sum, current_sum)
    
    return max_sum