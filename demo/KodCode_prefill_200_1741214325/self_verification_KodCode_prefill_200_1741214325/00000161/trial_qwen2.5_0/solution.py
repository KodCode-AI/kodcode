from itertools import combinations

def generate_combinations(numbers):
    """
    Generate all possible combinations of a given list of numbers including the empty set.
    :param numbers: List of numbers to generate combinations from.
    :return: A list of tuples, each representing a combination.
    """
    all_combinations = []
    for r in range(len(numbers) + 1):
        for combo in combinations(numbers, r):
            all_combinations.append(combo)
    return all_combinations