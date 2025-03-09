def find_missing_element(nums):
    """
    Finds the missing element in the array which is sorted in ascending order except for
    one missing number. The array contains integers from 1 to n inclusive, where n is the
    length of the array + 1 due to the missing number.
    """
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum