def calculate_paths(n: int) -> int:
    """
    Returns the number of unique paths in an n x n grid.
    """
    import math
    
    # The number of unique paths in an n x n grid can be calculated using the formula:
    # C(2n, n) = (2n)! / (n! * n!)
    # This is because we need to make a total of 2n moves (n down and n right),
    # and we need to choose n positions out of 2n for either type of move.
    total_moves = 2 * n
    down_moves = n
    # Calculate the number of paths using the formula for combinations
    paths = math.comb(total_moves, down_moves)
    return paths