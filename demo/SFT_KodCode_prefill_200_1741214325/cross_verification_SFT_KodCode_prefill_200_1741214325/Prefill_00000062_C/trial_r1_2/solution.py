from typing import List

def second_maximum(numbers: List[int]) -> int:
    unique = set(numbers)
    if len(unique) < 2:
        return None
    sorted_unique = sorted(unique)
    return sorted_unique[-2]