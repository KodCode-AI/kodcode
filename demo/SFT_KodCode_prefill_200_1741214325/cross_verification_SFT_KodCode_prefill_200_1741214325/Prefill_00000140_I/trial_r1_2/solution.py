def find_index_of_five(nums):
    try:
        return nums.index(5)
    except ValueError:
        return -1