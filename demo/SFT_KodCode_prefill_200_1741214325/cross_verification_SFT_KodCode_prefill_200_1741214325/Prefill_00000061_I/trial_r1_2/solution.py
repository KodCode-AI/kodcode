def find_first_unique(arr):
    if not arr:
        return -1
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    for num in arr:
        if counts[num] == 1:
            return num
    return -1