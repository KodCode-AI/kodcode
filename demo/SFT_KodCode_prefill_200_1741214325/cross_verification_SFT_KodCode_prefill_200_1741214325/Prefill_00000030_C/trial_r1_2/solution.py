from typing import List

def are_elements_unique(arr: List[int]) -> bool:
    return len(set(arr)) == len(arr)