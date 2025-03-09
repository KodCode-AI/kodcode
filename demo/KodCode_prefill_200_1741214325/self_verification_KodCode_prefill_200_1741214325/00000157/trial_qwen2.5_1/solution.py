def sum_even_sublists(lst):
    """
    Given a list of lists, return the sum of all numbers in the sublists that have an even number of elements.
    """
    total_sum = 0
    for sublist in lst:
        if len(sublist) % 2 == 0:
            total_sum += sum(sublist)
    return total_sum