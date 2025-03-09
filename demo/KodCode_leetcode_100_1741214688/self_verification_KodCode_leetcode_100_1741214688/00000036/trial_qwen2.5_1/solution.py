def min_flips_to_alternate(s: str) -> int:
    """
    Given a binary string, return the minimum number of operations needed to make the string alternating.
    If it is not possible, return -1.
    """
    n = len(s)
    
    if n == 0:
        return 0
    
    # Count differences with '010101...' pattern
    count_r = sum(s[i] != ('0' if i % 2 == 0 else '1') for i in range(n))
    
    # Count differences with '101010...' pattern
    count_l = sum(s[i] != ('1' if i % 2 == 0 else '0') for i in range(n))
    
    if count_r == n or count_l == n:
        return -1  # The string cannot be made alternating by flipping
    else:
        return min(count_r, count_l)