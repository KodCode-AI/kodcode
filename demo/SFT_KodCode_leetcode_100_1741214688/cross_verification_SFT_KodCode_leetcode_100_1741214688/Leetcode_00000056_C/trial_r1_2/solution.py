from typing import List

def max_distinct_elements_in_subarray(nums: List[int], k: int) -> int:
    if k == 0 or len(nums) == 0 or k > len(nums):
        return 0
    
    max_distinct = 0
    current_counts = {}
    distinct = 0
    
    # Initialize the first window
    for i in range(k):
        num = nums[i]
        if num not in current_counts:
            distinct += 1
        current_counts[num] = current_counts.get(num, 0) + 1
    
    max_distinct = distinct
    
    # Slide the window
    for i in range(1, len(nums) - k + 1):
        # Remove the leftmost element
        left = nums[i - 1]
        current_counts[left] -= 1
        if current_counts[left] == 0:
            distinct -= 1
            del current_counts[left]
        
        # Add the new rightmost element
        right = nums[i + k - 1]
        if right not in current_counts:
            distinct += 1
        current_counts[right] = current_counts.get(right, 0) + 1
        
        # Update the maximum distinct count
        if distinct > max_distinct:
            max_distinct = distinct
    
    return max_distinct