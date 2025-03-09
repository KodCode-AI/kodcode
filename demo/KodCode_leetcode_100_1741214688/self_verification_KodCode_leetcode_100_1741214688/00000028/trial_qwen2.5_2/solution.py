def min_swaps_to_group_ones(s: str) -> int:
    """
    Returns the minimum number of swaps required to group all '1's into a contiguous substring.
    """
    ones_count = s.count('1')
    max_ones_in_window = window_sum = 0
    left = 0
    
    for right in range(len(s)):
        window_sum += s[right] == '1'
        
        if right - left + 1 > ones_count:
            window_sum -= s[left] == '1'
            left += 1
        
        max_ones_in_window = max(max_ones_in_window, window_sum)
    
    return ones_count - max_ones_in_window