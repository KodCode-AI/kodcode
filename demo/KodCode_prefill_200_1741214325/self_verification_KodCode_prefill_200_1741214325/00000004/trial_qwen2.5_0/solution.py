def sum_recursive(lst):
    """
    Returns the sum of all numbers in a list using recursion.
    """
    if not lst:
        return 0
    else:
        return lst[0] + sum_recursive(lst[1:])