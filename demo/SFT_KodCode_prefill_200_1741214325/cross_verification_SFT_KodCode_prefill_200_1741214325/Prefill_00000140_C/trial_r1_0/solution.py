from typing import List

def find_index_of_five(numbers: List[int]) -> int:
    for index, number in enumerate(numbers):
        if number == 5:
            return index
    return -1