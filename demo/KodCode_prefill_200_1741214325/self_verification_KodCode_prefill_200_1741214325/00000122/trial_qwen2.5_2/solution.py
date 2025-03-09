def find_max_recursive(arr, n):
    """
    Returns the maximum number in an array using recursion.
    
    :param arr: List of integers
    :param n: Number of elements in the array to consider
    :return: Maximum integer in the array
    """
    # Base case: if the array has only one element
    if n == 1:
        return arr[0]
    
    # Recursive case: find the maximum in the rest of the array
    max_in_rest = find_max_recursive(arr, n-1)
    
    # Return the greater of the last element and the max of the rest
    return max(arr[n-1], max_in_rest)