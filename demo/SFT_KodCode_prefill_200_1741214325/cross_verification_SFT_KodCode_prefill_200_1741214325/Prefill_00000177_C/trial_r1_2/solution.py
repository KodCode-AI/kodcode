from typing import List

def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = []
    right = []
    for num in arr[:-1]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)
    return quick_sort(left) + [pivot] + quick_sort(right)