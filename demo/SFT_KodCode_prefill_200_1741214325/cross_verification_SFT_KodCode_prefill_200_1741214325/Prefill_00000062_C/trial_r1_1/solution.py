from typing import List

def second_maximum(numbers: List[int]) -> int:
    """ Returns the second maximum number in a list of integers.
    If the list does not contain at least two different numbers, returns None.
    """
    unique = set(numbers)
    if len(unique) < 2:
        return None
    max_num = max(numbers)
    less = [x for x in numbers if x < max_num]
    second_max = max(less)
    return second_max