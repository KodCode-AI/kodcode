def min_operations_to_equal_elements(nums):
    """
    Returns the minimum number of operations required to make all elements in nums equal.
    An operation consists of incrementing or decrementing an element by 1.
    """
    return sum(abs(nums[0] - num) for num in nums)