def flip_and_invert_image(grid):
    """
    Flips the given binary matrix horizontally and inverts the values.
    """
    m, n = len(grid), len(grid[0])
    result = []
    for row in grid:
        flipped_row = row[::-1]  # Flip horizontally
        inverted_row = [1 - val for val in flipped_row]  # Invert values
        result.append(inverted_row)
    return result