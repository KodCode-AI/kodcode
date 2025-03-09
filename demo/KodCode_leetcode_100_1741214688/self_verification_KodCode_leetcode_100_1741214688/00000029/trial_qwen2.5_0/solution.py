def longest_balanced_substring(s: str, k: int) -> int:
    """
    Finds the longest balanced substring that can be obtained by flipping at most k characters.
    A balanced substring is one with equal numbers of '0's and '1's.
    """
    max_length = 0
    zero_count = one_count = 0
    left = 0
    
    for right in range(len(s)):
        if s[right] == '0':
            zero_count += 1
        else:
            one_count += 1
        
        # If the window is not balanced and more flips are needed
        while zero_count > one_count + k and left <= right:
            if s[left] == '0':
                zero_count -= 1
            else:
                one_count -= 1
            left += 1
        
        # Update the maximum length of balanced substring found so far
        max_length = max(max_length, zero_count + one_count)
    
    return max_length * 2