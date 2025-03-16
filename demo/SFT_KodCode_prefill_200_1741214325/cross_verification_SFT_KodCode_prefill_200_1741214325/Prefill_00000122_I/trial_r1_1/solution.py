def find_max_recursive(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], max_in_array(arr[1:]))