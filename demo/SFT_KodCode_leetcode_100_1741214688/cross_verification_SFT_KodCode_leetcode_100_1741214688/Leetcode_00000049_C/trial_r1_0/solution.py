from collections import deque

def shortest_subarray_with_sum_at_least_target(nums, target):
    prefix_sum = [0]
    for num in nums:
        prefix_sum.append(prefix_sum[-1] + num)
    
    dq = deque()
    min_length = float('inf')
    
    for j in range(len(prefix_sum)):
        # Maintain deque in increasing order of prefix_sum
        while dq and prefix_sum[j] <= prefix_sum[dq[-1]]:
            dq.pop()
        dq.append(j)
        
        # Check if current prefix_sum can form a valid subarray
        while dq and prefix_sum[j] - prefix_sum[dq[0]] >= target:
            current_length = j - dq.popleft()
            if current_length < min_length:
                min_length = current_length
    
    return min_length if min_length != float('inf') else 0