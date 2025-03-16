from collections import defaultdict

def max_distinct_elements_in_subarray(nums, k):
    if k == 0:
        return 0
    freq = defaultdict(int)
    left = 0
    max_distinct = 0
    current_distinct = 0
    n = len(nums)
    for right in range(n):
        num = nums[right]
        if freq[num] == 0:
            current_distinct += 1
        freq[num] += 1

        # If window exceeds size k, move left pointer to the right
        while right - left + 1 > k:
            left_num = nums[left]
            freq[left_num] -= 1
            if freq[left_num] == 0:
                current_distinct -= 1
            left += 1

        # Check if the current window is exactly size k
        if right - left + 1 == k:
            max_distinct = max(max_distinct, current_distinct)
    return max_distinct