def sum_even_length_sublists(list_of_lists):
    """
    Given a list of lists, returns the sum of all numbers in the sublists that have an even number of elements.

    :param list_of_lists: A list containing sublists of integers.
    :return: The sum of all numbers in the sublists that have an even number of elements.
    """
    total_sum = 0
    for sublist in list_of_lists:
        if len(sublist) % 2 == 0:
            total_sum += sum(sublist)
    return total_sum