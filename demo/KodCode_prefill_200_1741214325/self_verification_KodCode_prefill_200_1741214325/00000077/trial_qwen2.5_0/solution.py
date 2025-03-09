def sort_2d_list(lst):
    """
    Sorts a 2D list such that each sublist within the list is sorted in increasing order based on the sum of its elements.
    """
    return sorted(lst, key=lambda x: sum(x))