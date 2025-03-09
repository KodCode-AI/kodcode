def binary_search(arr, target):
    """
    Performs a binary search on a sorted list of integers to find the index of the target value.
    Returns the index of the target value if found, or -1 if the target is not present.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1