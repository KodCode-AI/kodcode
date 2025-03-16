from collections import Counter

def find_first_unique(arr: list[int]) -> int:
    if not arr:
        return -1
    count = Counter(arr)
    for idx, num in enumerate(arr):
        if count[num] == 1:
            return idx
    return -1