def min_operations_to_equal_elements(arr):
    """
    Returns the minimum number of operations required to make all elements in the list equal.
    An operation is defined as incrementing or decrementing any element by 1.
    """
    return sum(abs(arr[0] - x) for x in arr)