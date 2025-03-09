def binary_search(sorted_list, target):
    """
    Performs a binary search on a sorted list to find the target value.
    Returns the index of the target if found, otherwise returns -1.
    """
    left, right = 0, len(sorted_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] < target:
            left = mid + 1
        elif sorted_list[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1