from collections import defaultdict

def max_distinct_elements_in_subarray(nums: list[int], k: int) -> int:
    if k == 0 or len(nums) < k:
        return 0
    
    count_map = defaultdict(int)
    max_distinct = 0
    current_distinct = 0
    left = 0
    
    for right in range(len(nums)):
        num = nums[right]
        if count_map[num] == 0:
            current_distinct += 1
        count_map[num] += 1
        
        # Ensure the window size does not exceed k
        while right - left + 1 > k:
            left_num = nums[left]
            count_map[left_num] -= 1
            if count_map[left_num] == 0:
                current_distinct -= 1
            left += 1
        
        # Update max_distinct if the current window is exactly size k
        if right - left + 1 == k:
            if current_distinct > max_distinct:
                max_distinct = current_distinct
    
    return max_distinct