def sort_tuples_by_second_item(tuples_list):
    """
    Sorts a list of tuples based on the second item in each tuple in ascending order.
    If two tuples have the same second item, it sorts them by the first item in ascending order.
    
    :param tuples_list: List of tuples to be sorted
    :return: Sorted list of tuples
    """
    return sorted(tuples_list, key=lambda x: (x[1], x[0]))