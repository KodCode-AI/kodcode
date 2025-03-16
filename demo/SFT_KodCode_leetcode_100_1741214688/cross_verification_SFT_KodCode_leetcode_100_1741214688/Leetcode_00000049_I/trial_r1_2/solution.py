from collections import deque

def shortest_subarray_with_sum_at_least_target(nums, target):
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    
    min_length = float('inf')
    dq = deque()
    
    len_prefix = len(prefix)
    
    for j in range(len_prefix):
        s = prefix[j] - target
        
        # Find the largest index in deque where the index <= j-2
        low_deque = 0
        high_deque = len(dq) - 1
        upper = -1
        
        while low_deque <= high_deque:
            mid_deque = (low_deque + high_deque) // 2
            if dq[mid_deque] <= j - 2:
                upper = mid_deque
                low_deque = mid_deque + 1
            else:
                high_deque = mid_deque - 1
        
        if upper != -1:
            low_i, high_i = 0, upper
            found = -1
            while low_i <= high_i:
                mid_i = (low_i + high_i) // 2
                if prefix[dq[mid_i]] <= s:
                    found = dq[mid_i]
                    low_i = mid_i + 1
                else:
                    high_i = mid_i - 1
            
            if found != -1:
                current_length = j - found
                if current_length >= 2:
                    if current_length < min_length:
                        min_length = current_length
        
        # Maintain deque in increasing order of prefix
        while dq and prefix[dq[-1]] >= prefix[j]:
            dq.pop()
        dq.append(j)
    
    return min_length if min_length != float('inf') else 0