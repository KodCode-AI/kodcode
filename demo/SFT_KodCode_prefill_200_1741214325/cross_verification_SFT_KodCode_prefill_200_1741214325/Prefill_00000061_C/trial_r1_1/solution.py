from collections import Counter
from typing import List

def find_first_unique(arr: List[int]) -> int:
    counts = Counter(arr)
    for index, num in enumerate(arr):
        if counts[num] == 1:
            return index
    return -1