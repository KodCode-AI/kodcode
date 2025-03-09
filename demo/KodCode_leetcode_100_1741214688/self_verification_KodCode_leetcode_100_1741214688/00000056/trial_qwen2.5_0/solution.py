from collections import Counter

def max_distinct_elements(nums, k):
    """
    Returns the maximum number of distinct elements in any continuous subarray of size k.
    """
    if k == 0:
        return 0
    window_counter = Counter(nums[:k])
    max_distinct = len(window_counter)
    for i in range(k, len(nums)):
        window_counter[nums[i]] += 1
        window_counter[nums[i - k]] -= 1
        if window_counter[nums[i - k]] == 0:
            del window_counter[nums[i - k]]
        max_distinct = max(max_distinct, len(window_counter))
    return max_distinct