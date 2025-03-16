from collections import defaultdict

def max_distinct_elements_in_subarray(nums: list[int], k: int) -> int:
    if k == 0 or len(nums) == 0:
        return 0
    
    freq = defaultdict(int)
    current_distinct = 0
    max_distinct = 0
    left = 0
    
    for right in range(len(nums)):
        num = nums[right]
        if freq[num] == 0:
            current_distinct += 1
        freq[num] += 1
        
        # Check if window exceeds size k
        while right - left + 1 > k:
            left_num = nums[left]
            freq[left_num] -= 1
            if freq[left_num] == 0:
                current_distinct -= 1
            left += 1
        
        # Update max when window is exactly size k
        if right - left + 1 == k:
            if current_distinct > max_distinct:
                max_distinct = current_distinct
    
    return max_distinct