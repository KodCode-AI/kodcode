def optimized_solution(limit: int) -> int:
    """
    Returns the number of right triangles that can be formed on a grid
    from the origin with coordinates between 0 and limit inclusive.
    """
    count = 0
    # Iterate over all possible x1, y1, x2, y2 within the given limit
    for x1 in range(limit + 1):
        for y1 in range(limit + 1):
            for x2 in range(limit + 1):
                for y2 in range(limit + 1):
                    if (x1, y1) != (x2, y2) and (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) == (x1 * x1 + y1 * y1):
                        count += 1
    return count