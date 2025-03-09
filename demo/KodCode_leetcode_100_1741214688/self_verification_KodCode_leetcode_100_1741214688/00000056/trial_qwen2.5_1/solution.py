from collections import defaultdict

def max_distinct_elements_in_subarray(nums, k):
    """
    Given an unsorted array of integers and a positive integer k, returns the maximum number of distinct elements
    in any continuous subarray of size k.
    """
    if k == 0:
        return 0
    distinct_count = defaultdict(int)
    max_distinct = 0
    left = 0
    
    for right in range(len(nums)):
        distinct_count[nums[right]] += 1
        while right - left + 1 > k:
            distinct_count[nums[left]] -= 1
            if distinct_count[nums[left]] == 0:
                del distinct_count[nums[left]]
            left += 1
        max_distinct = max(max_distinct, len(distinct_count))
    
    return max_distinct