def can_win_game(cevablar):
    """
    Checks if a given set of cevablar can win the game.
    
    Parameters:
    cevablar (list): A list containing the number of blueblocks, greenblocks, and redblocks.
    
    Returns:
    bool: True if the given set can win the game, False otherwise.
    """
    blueblocks, greenblocks, redblocks = cevablar
    # A player can win if they can form a sequence of blocks such that each block is of a different color
    # This means there should be at least one block of each color
    return blueblocks > 0 and greenblocks > 0 and redblocks > 0