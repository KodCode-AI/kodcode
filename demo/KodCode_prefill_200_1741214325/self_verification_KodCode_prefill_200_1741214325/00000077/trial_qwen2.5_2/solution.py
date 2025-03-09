def sort_2d_list(our_list):
    """
    Returns a new 2D list sorted by the increasing sum of elements in each sublist.
    """
    return sorted(our_list, key=sum)