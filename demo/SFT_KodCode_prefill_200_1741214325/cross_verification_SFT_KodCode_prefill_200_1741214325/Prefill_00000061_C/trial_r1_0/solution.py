from typing import List

def find_first_unique(arr: List[int]) -> int:
    if not arr:
        return -1
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    for index, num in enumerate(arr):
        if freq[num] == 1:
            return index
    return -1