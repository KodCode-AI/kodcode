def f(x, nums):
    """
    Returns the number of elements in nums that are strictly less than x.
    """
    return len([num for num in nums if num < x])

def result_array(nums):
    """
    For each element in nums, compute the number of elements strictly less than it,
    then sum these values across all elements in the array.
    """
    n = len(nums)
    result = [0] * n
    for i in range(n):
        result[i] = sum(f(nums[i], nums[:i]) + f(nums[i], nums[i+1:]))
    return result