def find_index_of_five(lst):
    for index, value in enumerate(lst):
        if value == 5:
            return index
    return -1