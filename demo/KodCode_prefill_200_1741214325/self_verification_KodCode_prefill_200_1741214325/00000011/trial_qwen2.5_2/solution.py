def max_product_subarray(nums):
    """
    Returns the maximum product of a contiguous subarray within the input array.
    """
    if not nums:
        return 0

    max_product = min_product = result = nums[0]

    for num in nums[1:]:
        candidates = (max_product * num, min_product * num, num)
        max_product = max(candidates)
        min_product = min(candidates)
        result = max(result, max_product)

    return result