def max_subarray_sum(arr):
    if not arr:
        return None
    max_so_far = current_max = arr[0]
    for num in arr[1:]:
        current_max = max(num, current_max + num)
        max_so_far = max(max_so_far, current_max)
    return max_so_far