def count_paths(m: int, n: int) -> int:
    """ Returns the number of unique paths from the top-left corner to the bottom-right corner
    of an M x N grid, where movement is restricted to only down or right."""
    if m == 1 or n == 1:
        return 1
    a = m + n - 2
    b = min(m - 1, n - 1)
    result = 1
    for i in range(1, b + 1):
        result = result * (a - b + i) // i
    return result