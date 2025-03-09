from itertools import combinations

def generate_combinations(numbers):
    """
    Generates all possible combinations of the given list of numbers.
    """
    all_combinations = []
    for r in range(1, len(numbers) + 1):
        all_combinations.extend(combinations(numbers, r))
    return all_combinations