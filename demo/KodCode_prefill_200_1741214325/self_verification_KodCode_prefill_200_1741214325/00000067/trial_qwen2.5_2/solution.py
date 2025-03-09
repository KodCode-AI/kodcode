def sum_of_evens(lst):
    """
    Returns the sum of all even numbers in the given list.
    """
    return sum([x for x in lst if x % 2 == 0])