def find_index_of_five(numbers):
    """
    Returns the index of the first occurrence of the number 5 in the list.
    If 5 is not found, returns -1.
    """
    try:
        return numbers.index(5)
    except ValueError:
        return -1