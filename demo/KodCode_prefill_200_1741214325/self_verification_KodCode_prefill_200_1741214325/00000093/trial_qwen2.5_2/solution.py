def find_smallest_number(arr):
    """
    Returns the smallest number in an array of integers.
    
    Parameters:
    arr (list of int): The array of integers.
    
    Returns:
    int: The smallest number in the array.
    """
    if not arr:  # Check if the array is empty
        return None
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest