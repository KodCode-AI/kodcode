def optimized_solution(limit: int) -> int:
    """
    Returns the number of right triangles OPQ that can be formed with
    coordinates (x1, y1) and (x2, y2) in the range [0, limit].
    """
    count = 0
    for x in range(limit + 1):
        for y in range(limit + 1):
            # Count triangles with x-axis as the base
            count += min(x, limit - x) * min(y, limit - y)
            # Count triangles with y-axis as the base
            count += min(y, limit - y) * min(x, limit - x)
    return count * 2