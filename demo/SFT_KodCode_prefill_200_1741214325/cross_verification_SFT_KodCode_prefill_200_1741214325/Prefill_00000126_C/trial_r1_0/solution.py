from typing import List

def is_sorted_ascending(numbers: List[int]) -> bool:
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True