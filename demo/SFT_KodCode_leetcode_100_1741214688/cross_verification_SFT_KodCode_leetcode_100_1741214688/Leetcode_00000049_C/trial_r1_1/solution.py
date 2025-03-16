from typing import List
from collections import deque

def shortest_subarray_with_sum_at_least_target(nums: List[int], target: int) -> int:
    # Check if any single element meets or exceeds the target
    for num in nums:
        if num >= target:
            return 1
    
    # Compute the prefix sum array
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    
    min_length = float('inf')
    dq = deque()
    dq.append(0)  # Initialize the deque with the first index
    
    for j in range(1, len(prefix)):
        # Check if the current prefix sum minus the front of the deque meets the target
        while dq and prefix[j] - prefix[dq[0]] >= target:
            current_length = j - dq.popleft()
            if current_length < min_length:
                min_length = current_length
        
        # Maintain the deque to ensure it's in increasing order of prefix sums
        while dq and prefix[j] <= prefix[dq[-1]]:
            dq.pop()
        
        dq.append(j)
    
    if min_length != float('inf'):
        return min_length
    else:
        return 0