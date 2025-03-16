def can_win_game(cevablar):
    # Initialize the game with one block of each color
    blue, green, red = 1, 1, 1
    previous_color = None
    
    for color in cevablar:
        # Check if the current move is allowed based on the previous color
        if previous_color == 'blue':
            if color != 'blue':
                return False
        elif previous_color == 'green':
            if color not in ['green', 'red']:
                return False
        elif previous_color == 'red':
            # Game should have ended before
            return False
        
        # Check if the color is available
        if (color == 'blue' and blue == 0) or \
           (color == 'green' and green == 0) or \
           (color == 'red' and red == 0):
            return False
        
        # Remove one block of the chosen color
        if color == 'blue':
            blue -= 1
        elif color == 'green':
            green -= 1
        elif color == 'red':
            red -= 1
        
        # Check for winning conditions after this move
        win = False
        if color == 'blue':
            # Next player must move blue, but if there are none, they lose
            if blue == 0:
                win = True
        elif color == 'green':
            # Next player can move green or red; if both are empty, they lose
            if green == 0 and red == 0:
                win = True
        elif color == 'red':
            # Win only if all blocks are removed with this move
            if blue == 0 and green == 0 and red == 0:
                win = True
            else:
                # Removing red with other blocks left is a losing move
                return False
        
        if win:
            return True
        
        previous_color = color
    
    # No winning move found in the sequence
    return False