def find_max_recursive(arr):
    """
    Recursively find the maximum number in an array.
    
    :param arr: List of numbers
    :return: Maximum number in the array
    """
    if len(arr) == 1:
        return arr[0]
    else:
        sub_max = find_max_recursive(arr[1:])
        return arr[0] if arr[0] > sub_max else sub_max