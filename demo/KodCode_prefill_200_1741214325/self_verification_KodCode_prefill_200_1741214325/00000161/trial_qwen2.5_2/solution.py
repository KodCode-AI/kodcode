from itertools import combinations

def generate_combinations(numbers):
    """
    Generates all possible combinations of a given list of numbers.
    
    :param numbers: List of integers
    :return: A list of lists, where each sublist is a combination of the input numbers
    """
    all_combinations = []
    for r in range(len(numbers) + 1):
        all_combinations.extend(combinations(numbers, r))
    return all_combinations