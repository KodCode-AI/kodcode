def min_operations_to_equal_elements(nums):
    """
    Returns the minimum number of operations required to make all elements in the list equal.
    Each operation consists of incrementing or decrementing an element by 1.
    """
    return sum(abs(nums[i] - min(nums)) for i in range(len(nums)))