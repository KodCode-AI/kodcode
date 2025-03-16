from collections import defaultdict

def max_distinct_elements_in_subarray(nums, k):
    freq = defaultdict(int)
    left = 0
    max_distinct = 0
    current_distinct = 0

    for right in range(len(nums)):
        num = nums[right]
        if freq[num] == 0:
            current_distinct += 1
        freq[num] += 1

        # Ensure the window size does not exceed k
        while (right - left + 1) > k:
            left_num = nums[left]
            freq[left_num] -= 1
            if freq[left_num] == 0:
                current_distinct -= 1
            left += 1

        # Check if the window size is exactly k
        if (right - left + 1) == k:
            if current_distinct > max_distinct:
                max_distinct = current_distinct

    return max_distinct