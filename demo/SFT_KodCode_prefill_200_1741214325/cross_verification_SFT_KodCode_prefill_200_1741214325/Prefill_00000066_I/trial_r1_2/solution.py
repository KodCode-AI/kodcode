def max_subarray_sum(arr):
    if not arr:
        return None  # handles empty array case, can return 0 depending on requirements
    current_max = max_sum = arr[0]
    for num in arr[1:]:
        current_max = max(num, current_max + num)
        max_sum = max(max_sum, current_max)
    return max_sum