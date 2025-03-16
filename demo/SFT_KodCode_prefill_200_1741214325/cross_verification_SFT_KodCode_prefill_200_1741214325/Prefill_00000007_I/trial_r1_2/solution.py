def can_win_game(cevablar, obstacles):
    blue, green, red = cevablar
    current = 0
    n = len(obstacles)
    
    while current < n:
        max_reach = current
        next_block = None
        
        # Try blue blocks
        if blue > 0:
            reach = current + 1
            while reach < n and (obstacles[reach] == 'B' or obstacles[reach] == ' '):
                if obstacles[reach] == 'B':
                    blue -= 1
                reach += 1
            if reach > max_reach:
                max_reach = reach
                next_block = 'B'
        
        # Try green blocks
        if green > 0:
            reach = current + 1
            while reach < n and (obstacles[reach] == 'G' or obstacles[reach] == ' '):
                if obstacles[reach] == 'G':
                    green -= 1
                reach += 1
            if reach > max_reach:
                max_reach = reach
                next_block = 'G'
        
        # Try red blocks
        if red > 0:
            reach = current + 1
            while reach < n and (obstacles[reach] == 'R' or obstacles[reach] == ' '):
                if obstacles[reach] == 'R':
                    red -= 1
                reach += 1
            if reach > max_reach:
                max_reach = reach
                next_block = 'R'
        
        # If no block can be used, the game can't proceed
        if max_reach == current:
            return False
        
        current = max_reach
    
    return True