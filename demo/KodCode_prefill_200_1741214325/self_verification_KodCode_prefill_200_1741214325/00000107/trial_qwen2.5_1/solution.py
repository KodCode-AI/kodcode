def find_pairs_with_sum(numbers, target):
    """
    Returns a list of tuples representing the pairs of numbers in 'numbers' that sum to 'target'.
    """
    seen = set()
    pairs = set()
    for number in numbers:
        complement = target - number
        if complement in seen:
            pairs.add((min(number, complement), max(number, complement)))
        seen.add(number)
    return list(pairs)