from typing import List

def find_max_recursive(arr: List[int], n: int) -> int:
    """ Uses recursion to find the maximum number in the array.
    Args:
        arr: List of integers.
        n: Number of elements in the array to consider for finding the maximum.
    
    Returns:
        The maximum number in the array.
    """
    if n == 1:
        return arr[0]
    else:
        max_rest = find_max_recursive(arr, n - 1)
        return max(max_rest, arr[n - 1])