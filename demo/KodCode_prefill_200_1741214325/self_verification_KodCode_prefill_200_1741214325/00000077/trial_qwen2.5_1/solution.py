def sort_2d_list(input_list):
    """
    Sorts a 2D list based on the sum of elements in each sublist in increasing order.
    
    :param input_list: A 2D list where each sublist contains numeric elements.
    :return: A 2D list sorted based on the sum of elements in each sublist.
    """
    return sorted(input_list, key=sum)