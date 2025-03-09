def optimized_integer_square_root(num: int) -> int:
    if num < 0:
        raise ValueError("Input must be a non-negative integer.")
    if num == 0 or num == 1:
        return num
    
    low, high = 1, num // 2
    
    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid
        
        if mid_squared == num:
            return mid
        elif mid_squared < num:
            low = mid + 1
        else:
            high = mid - 1
    
    return high