def find_max_recursive(array):
    if len(array) == 1:
        return array[0]
    else:
        return array[0] if array[0] > find_max(array[1:]) else find_max(array[1:])