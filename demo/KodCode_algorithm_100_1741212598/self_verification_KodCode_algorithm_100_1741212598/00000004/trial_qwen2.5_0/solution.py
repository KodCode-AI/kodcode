def optimized_integer_square_root(num: int) -> int:
    if num < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    if num == 0:
        return 0
    
    if num == 1:
        return 1
    
    if num == num ** 0.5:
        return int(num ** 0.5)
    
    left, right = 1, num // 2
    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid
        
        if mid_squared == num:
            return mid
        elif mid_squared < num:
            left = mid + 1
            result = mid
        else:
            right = mid - 1
    
    return result