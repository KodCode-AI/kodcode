def cube_root(n: int) -> int:
    """
    Returns the cube root of n if n is a perfect cube, otherwise returns None.
    """
    if not isinstance(n, int):
        raise TypeError("cube_root() only accepts integers")
    if n < 0:
        n = -n

    if n == 0:
        return 0

    left = 1
    right = n

    while left <= right:
        mid = left + (right - left) // 2
        cube = mid * mid * mid

        if cube == n:
            return mid
        elif cube < n:
            left = mid + 1
        else:
            right = mid - 1

    return None