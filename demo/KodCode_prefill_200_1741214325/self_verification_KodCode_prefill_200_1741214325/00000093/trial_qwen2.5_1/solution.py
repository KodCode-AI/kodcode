def find_smallest_number(arr):
    """
    Returns the smallest number in the given array of integers.
    """
    if not arr:
        raise ValueError("Array must not be empty")
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest