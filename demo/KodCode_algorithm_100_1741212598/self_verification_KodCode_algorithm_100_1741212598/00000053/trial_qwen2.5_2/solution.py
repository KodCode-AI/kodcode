from math import comb

def max_prize_fund(num_turns: int) -> int:
    """
    Calculates the maximum prize fund that should be allocated for a single game.
    """
    total_probability = 0
    for i in range(1, num_turns // 2 + 1):
        probability = comb(num_turns, i) * (1 / 2) ** num_turns
        total_probability += probability
    
    # The expected value of the game should be 0, so prize_fund - 1 = total_probability
    prize_fund = int(1 / total_probability)
    return prize_fund