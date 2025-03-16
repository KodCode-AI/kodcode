from typing import List

def is_sorted_ascending(numbers: List[int]) -> bool:
    for a, b in zip(numbers, numbers[1:]):
        if a > b:
            return False
    return True