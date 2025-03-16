from collections import defaultdict

def max_distinct_elements_in_subarray(nums, k):
    n = len(nums)
    if k == 0 or k > n:
        return 0
    freq = defaultdict(int)
    distinct = 0
    # Initialize the first window
    for i in range(k):
        num = nums[i]
        if freq[num] == 0:
            distinct += 1
        freq[num] += 1
    max_distinct = distinct
    # Slide the window through the array
    for i in range(n - k):
        # Remove the leftmost element of the previous window
        left = nums[i]
        freq[left] -= 1
        if freq[left] == 0:
            distinct -= 1
        # Add the new right element
        right = nums[i + k]
        if freq[right] == 0:
            distinct += 1
        freq[right] += 1
        # Update the maximum number of distinct elements
        if distinct > max_distinct:
            max_distinct = distinct
    return max_distinct