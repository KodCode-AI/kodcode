from typing import List

def union_of_lists(list1: List[int], list2: List[int]) -> List[int]:
    result = []
    seen = set()
    for num in list1:
        if num not in seen:
            result.append(num)
            seen.add(num)
    for num in list2:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result