def sort_tuples(lst):
    """
    Sorts a list of tuples by the second item, then by the first item if the second items are equal.
    """
    return sorted(lst, key=lambda x: (x[1], x[0]))