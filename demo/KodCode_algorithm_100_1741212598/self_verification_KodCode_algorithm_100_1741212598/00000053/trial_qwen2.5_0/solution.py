from math import comb

def max_prize_fund(num_turns: int) -> int:
    """
    Calculates the maximum prize fund such that the expected loss is minimized.
    The player wins if they draw more blue discs than red discs after num_turns.
    The function returns the prize fund as an integer.
    """
    max_fund = 0
    for i in range(1, num_turns + 1):
        # Calculate the number of ways to win (more blue than red)
        blue_more_than_red = 0
        for blue_draws in range(1, i // 2 + 1):
            red_draws = i - 2 * blue_draws
            if i % 2 == 0 and red_draws < blue_draws:
                continue
            ways_to_win = comb(blue_draws + red_draws, blue_draws) * comb(red_draws + 1, red_draws + 1)
            blue_more_than_red += ways_to_win
        # Total number of ways to draw i discs
        total_ways = comb(2 * i - 1, i)
        # Probability of winning
        prob_win = blue_more_than_red / total_ways
        # Calculate the prize fund
        fund = int(1 / prob_win)  # Since the loss is £1
        max_fund = max(max_fund, fund)
    return max_fund