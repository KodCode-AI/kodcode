def find_max_recursive(array):
    if len(array) == 1:
        return array[0]
    return max(array[0], find_max(array[1:]))