def find_index_of_five(nums):
    for index, value in enumerate(nums):
        if value == 5:
            return index
    return -1