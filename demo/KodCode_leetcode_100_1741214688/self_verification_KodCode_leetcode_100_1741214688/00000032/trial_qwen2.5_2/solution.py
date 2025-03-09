def count_smaller(nums):
    """
    Given an integer array nums sorted in non-decreasing order, this function
    returns the result array where each element is the sum of 'f(nums[j])' for
    all j != i, where f(x) is the number of elements strictly less than x in nums.
    """
    # Create a copy of nums to track original indices
    indexed_nums = sorted(enumerate(nums), key=lambda x: x[1])
    result = [0] * len(nums)
    from sortedcontainers import SortedList
    sl = SortedList()
    
    for index, num in indexed_nums:
        # Get the count of elements strictly less than nums[index]
        count = sl.bisect_left(num)
        # Update the sum of f(nums[i]) for current index
        result[index] = sum(count for count in sl if count < num)
        # Add the current number to the sorted list
        sl.add(num)
    
    return result