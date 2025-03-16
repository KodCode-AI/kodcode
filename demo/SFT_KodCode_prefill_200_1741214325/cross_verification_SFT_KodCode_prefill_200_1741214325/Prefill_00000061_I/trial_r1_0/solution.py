def find_first_unique(array):
    counts = {}
    for num in array:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    for num in array:
        if counts[num] == 1:
            return num
    return -1