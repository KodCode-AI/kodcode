from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    arr_copy = arr.copy()
    n = len(arr_copy)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
        if not swapped:
            break
    return arr_copy