from math import comb

def max_prize_fund(num_turns: int) -> int:
    """
    Calculates the maximum prize fund that should be allocated for a single game.
    """
    prob_winning = 0
    for i in range(1, num_turns // 2 + 1):
        prob_winning += comb(num_turns, i) / (2 ** num_turns)
    return int(1 / prob_winning)