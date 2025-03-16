from typing import List

def sum_of_evens(numbers: List[int]) -> int:
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total