from collections import defaultdict

def max_distinct_elements(nums, k):
    """
    Return the maximum number of distinct elements in any continuous subarray of size k.
    """
    element_count = defaultdict(int)
    max_distinct = 0
    distinct_count = 0

    start = 0
    for end in range(len(nums)):
        element_count[nums[end]] += 1
        if element_count[nums[end]] == 1:
            distinct_count += 1

        if end >= k - 1:
            max_distinct = max(max_distinct, distinct_count)
            if element_count[nums[start]] == 1:
                distinct_count -= 1
            element_count[nums[start]] -= 1
            start += 1

    return max_distinct