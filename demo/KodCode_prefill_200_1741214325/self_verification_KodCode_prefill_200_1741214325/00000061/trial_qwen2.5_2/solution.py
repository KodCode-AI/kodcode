def find_non_repeated(arr):
    """
    Returns the index of the first non-repeated element in the array.
    If no such element exists, returns -1.
    """
    from collections import Counter
    counts = Counter(arr)
    for idx, value in enumerate(arr):
        if counts[value] == 1:
            return idx
    return -1