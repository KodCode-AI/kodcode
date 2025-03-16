def optimized_integer_square_root(num: int) -> int:
    if num < 0:
        raise ValueError("num must be non-negative")
    if num == 0 or num == 1:
        return num
    # Exponential search to find an upper bound
    high = 1
    while high * high <= num:
        high *= 2
    # Binary search within the found bounds
    low = high // 2
    while low <= high:
        mid = (low + high) // 2
        mid_sq = mid * mid
        if mid_sq == num:
            return mid
        elif mid_sq < num:
            low = mid + 1
        else:
            high = mid - 1
    return high