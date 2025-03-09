def can_win_game(cevablar):
    """
    Returns True if the given set of cevablar (list of integers representing the number of blueblocks, greenblocks, and redblocks) 
    can win a greedy game, otherwise returns False.
    A player wins if they can make more moves than their opponent.
    A move consists of picking either a blueblock (decrementing the blueblock count by 1), a greenblock (decrementing the greenblock count by 2), or a redblock (decrementing the redblock count by 3).
    """
    blueblocks, greenblocks, redblocks = cevablar
    total_blocks = blueblocks + greenblocks + redblocks
    green_blocks twice = greenblocks * 2
    red_blocks三次 = redblocks * 3
    
    # The opponent's initial number of moves would be the sum of all blocks
    opponent_moves = total_blocks
    
    # If the sum of all blocks is less than or equal to the opponent's initial moves, the player can't win
    if total_blocks <= opponent_moves:
        return False
    
    # The player's additional moves would be the sum of all blocks minus 2
    player_moves = total_blocks - 2
    
    # Calculate the total possible moves for the player considering the initial moves of the opponent
    player_possible_moves = (player_moves + 2) // 3 * 3 + (player_moves % 3 + 2) // 2 * 2 + player_moves % 3
    
    # If the player's total possible moves are greater than or equal to the opponent's moves, the player can win
    return player_possible_moves >= opponent_moves