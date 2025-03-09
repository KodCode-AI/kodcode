def can_win_greedy_game(blueblocks, greenblocks, redblocks):
    """
    Returns True if the given set of blocks can win the greedy game, 
    otherwise returns False. A player can win the game if they can 
    make a strictly increasing sequence of blocks, where each block's 
    value is greater than the previous block's value.
    """
    total_blocks = blueblocks + greenblocks + redblocks
    if total_blocks < 3:
        return False
    if blueblocks > 0 and greenblocks > 0 and redblocks > 0:
        return True
    if blueblocks > 0 and redblocks > 0:
        return True
    if greenblocks > 0 and redblocks > 0:
        return True
    return False