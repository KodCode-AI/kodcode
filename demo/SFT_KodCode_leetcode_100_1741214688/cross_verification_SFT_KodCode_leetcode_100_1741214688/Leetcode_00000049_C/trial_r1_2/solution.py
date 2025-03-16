from collections import deque
from typing import List

def shortest_subarray_with_sum_at_least_target(nums: List[int], target: int) -> int:
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    
    dq = deque()
    min_len = float('inf')
    
    for j in range(len(prefix)):
        # Maintain the deque to keep indices with increasing prefix sums
        while dq and prefix[j] <= prefix[dq[-1]]:
            dq.pop()
        dq.append(j)
        
        # Check for valid subarrays
        while dq and (prefix[j] - prefix[dq[0]] >= target):
            i = dq.popleft()
            current_length = j - i
            if current_length < min_len:
                min_len = current_length
    
    return min_len if min_len != float('inf') else 0