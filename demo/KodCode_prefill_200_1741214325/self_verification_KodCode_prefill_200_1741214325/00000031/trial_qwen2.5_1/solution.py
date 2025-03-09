def find_closest_element(arr, target):
    """
    Finds the closest element to the target in an almost sorted array.
    An almost sorted array is one where each element is no more than two positions away
    from its sorted position.
    
    Args:
    arr : List[int]
        The almost sorted array.
    target : int
        The target value to find the closest element to.
        
    Returns:
    int
        The closest element to the target in the array.
    """
    left, right = 0, len(arr) - 1
    closest_index = 0
    min_diff = float('inf')

    while left <= right:
        mid = (left + right) // 2
        # Check if the current element or its neighbors could be the closest
        if abs(arr[mid] - target) < min_diff:
            min_diff = abs(arr[mid] - target)
            closest_index = mid

        # Move the search towards the center
        if arr[mid] == target:
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return arr[closest_index]