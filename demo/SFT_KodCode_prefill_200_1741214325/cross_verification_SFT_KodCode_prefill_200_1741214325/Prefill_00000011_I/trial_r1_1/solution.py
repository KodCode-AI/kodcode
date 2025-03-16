def max_product_subarray(arr):
    if not arr:
        return 0  # or raise ValueError("Array is empty")
    current_max = current_min = max_product = arr[0]
    for num in arr[1:]:
        temp_max = max(num, current_max * num, current_min * num)
        temp_min = min(num, current_max * num, current_min * num)
        current_max, current_min = temp_max, temp_min
        if current_max > max_product:
            max_product = current_max
    return max_product