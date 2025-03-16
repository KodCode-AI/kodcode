from typing import List

def find_index_of_five(numbers: List[int]) -> int:
    try:
        return numbers.index(5)
    except ValueError:
        return -1