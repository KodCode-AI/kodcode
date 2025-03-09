def flip_and_invert_image(grid):
    """
    Flips the given binary matrix horizontally and inverts all the values.
    """
    flipped_inverted_grid = []
    for row in grid:
        # Reverse the row and invert the values
        flipped_inverted_row = [1 - val for val in reversed(row)]
        flipped_inverted_grid.append(flipped_inverted_row)
    return flipped_inverted_grid