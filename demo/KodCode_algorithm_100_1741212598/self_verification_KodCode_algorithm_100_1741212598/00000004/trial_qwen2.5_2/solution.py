def optimized_integer_square_root(num: int) -> int:
    """
    Returns the integer square root of a non-negative integer num.
    Raises ValueError for negative inputs.
    """
    if num < 0:
        raise ValueError("Input must be a non-negative integer.")
    if num == 0 or num == 1:
        return num
    
    lower_bound = 1
    upper_bound = num // 2
    
    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2
        mid_squared = mid * mid
        
        if mid_squared == num:
            return mid
        elif mid_squared < num:
            lower_bound = mid + 1
            result = mid
        else:
            upper_bound = mid - 1
    
    return result