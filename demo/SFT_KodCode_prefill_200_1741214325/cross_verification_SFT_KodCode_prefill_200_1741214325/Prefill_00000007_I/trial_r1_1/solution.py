import itertools

def can_win_game(blocks, target_points):
    point_values = {'blue': 1, 'green': 2, 'red': 3}
    colors_present = [color for color in blocks if blocks.get(color, 0) > 0]
    
    if not colors_present:
        return target_points <= 0
    
    max_score = 0
    
    for permutation in itertools.permutations(colors_present):
        temp_blocks = blocks.copy()
        current_score = 0
        
        for color in permutation:
            if temp_blocks.get(color, 0) <= 0:
                continue
            
            higher_sum = 0
            for other_color in colors_present:
                if other_color != color and temp_blocks.get(other_color, 0) > 0:
                    if point_values[other_color] > point_values[color]:
                        higher_sum += temp_blocks[other_color]
            
            current_score += temp_blocks[color] * higher_sum
            temp_blocks[color] = 0
            
            if current_score >= target_points:
                return True
        
        if current_score > max_score:
            max_score = current_score
            
            if max_score >= target_points:
                return True
    
    return max_score >= target_points