def find_missing_element(nums):
    """
    Finds the missing element in a sorted array of integers from 1 to n inclusive.
    """
    expected_sum = (len(nums) + 1) * (len(nums) + 2) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum