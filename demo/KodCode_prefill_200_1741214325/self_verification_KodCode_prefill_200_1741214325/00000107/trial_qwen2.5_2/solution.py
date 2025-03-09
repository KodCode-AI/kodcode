def find_pairs(numbers, target):
    """
    Returns a list of tuples, each containing a pair of numbers from 'numbers' that sum to 'target'.
    """
    pairs = []
    seen = set()
    for num in numbers:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs