def optimized_solution(limit: int) -> int:
    """
    Returns the number of right triangles that can be formed with the given limit.
    """
    total_triangles = 0
    max_x = limit + 1
    max_y = limit + 1

    # Counting triangles with horizontal or vertical legs
    for x in range(max_x):
        for y in range(max_y):
            total_triangles += x * y * (limit - x + 1) * (limit - y + 1)

    return total_triangles