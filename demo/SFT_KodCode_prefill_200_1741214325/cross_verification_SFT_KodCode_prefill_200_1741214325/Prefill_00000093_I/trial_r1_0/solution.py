def find_smallest_number(arr):
    if not arr:
        raise ValueError("Array is empty")
    return min(arr)