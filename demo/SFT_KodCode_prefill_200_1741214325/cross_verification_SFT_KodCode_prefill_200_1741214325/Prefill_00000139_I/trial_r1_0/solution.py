def max_subarray_kadane(arr):
    if not arr:
        return 0  # or raise ValueError("Array is empty")
    
    max_ending_here = max_so_far = arr[0]
    
    for num in arr[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far