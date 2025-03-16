def max_subarray_kadane(arr):
    if not arr:
        return 0  # Returns 0 for an empty array
    
    current_max = max_sum = arr[0]
    
    for num in arr[1:]:
        current_max = max(num, current_max + num)
        max_sum = max(max_sum, current_max)
    
    return max_sum