def max_subarray_kadane(arr):
    if not arr:
        return None  # Return None for an empty array
    current_max = global_max = arr[0]
    for num in arr[1:]:
        current_max = max(num, current_max + num)
        if current_max > global_max:
            global_max = current_max
    return global_max