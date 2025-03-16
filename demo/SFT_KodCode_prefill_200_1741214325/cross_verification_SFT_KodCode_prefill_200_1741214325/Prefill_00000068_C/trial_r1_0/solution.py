from typing import List

def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    less = [x for x in arr[:-1] if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr[:-1] if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)