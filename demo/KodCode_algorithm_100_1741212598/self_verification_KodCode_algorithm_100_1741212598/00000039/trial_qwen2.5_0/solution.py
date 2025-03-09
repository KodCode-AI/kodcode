def cube_root(n: int) -> int:
    """
    Returns the integer cube root of n if n is a perfect cube, otherwise returns None.
    """
    if not isinstance(n, int):
        raise TypeError("cube_root() only accepts integers")
    if n == 0:
        return 0  # Handle edge case for zero
    if n < 0:
        n = -n
        lower = -int(round(n ** (1/3.0)))
        upper = -1
    else:
        lower = 0
        upper = int(round(n ** (1/3.0)))

    while lower <= upper:
        mid = (lower + upper) // 2
        if mid * mid * mid == n:
            return mid
        elif mid * mid * mid < n:
            lower = mid + 1
        else:
            upper = mid - 1
    return None