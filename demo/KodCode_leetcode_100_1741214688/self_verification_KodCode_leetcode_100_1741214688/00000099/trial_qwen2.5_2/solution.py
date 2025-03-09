def flip_and_invert_image(grid):
    """
    Flips the given binary matrix horizontally, then inverts all the values.
    :param grid: List[List[int]] - The input binary matrix.
    :return: List[List[int]] - The flipped and inverted matrix.
    """
    m, n = len(grid), len(grid[0])
    result = []
    for row in grid:
        flipped_row = row[::-1]  # Flip the row horizontally
        inverted_row = [1 - val for val in flipped_row]  # Invert the values
        result.append(inverted_row)
    return result