def sort_tuples_list(tuples_list):
    """
    Sorts a list of tuples based on the second item in each tuple in ascending order.
    If two tuples have the same second item, they are sorted by their first item in ascending order.
    """
    return sorted(tuples_list, key=lambda x: (x[1], x[0]))