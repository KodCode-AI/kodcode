import heapq
from typing import List

def merge_sorted_lists(lst1: List[int], lst2: List[int]) -> List[int]:
    return list(heapq.merge(lst1, lst2))