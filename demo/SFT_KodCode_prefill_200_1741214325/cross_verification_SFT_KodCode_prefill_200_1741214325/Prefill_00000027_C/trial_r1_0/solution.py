from typing import List

def union_of_lists(list1: List[int], list2: List[int]) -> List[int]:
    combined = list1 + list2
    unique_elements = set(combined)
    return sorted(unique_elements)