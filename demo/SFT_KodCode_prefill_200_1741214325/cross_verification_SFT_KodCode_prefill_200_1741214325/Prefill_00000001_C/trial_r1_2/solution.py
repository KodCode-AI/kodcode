from typing import List

def selection_sort(arr: List[int]) -> List[int]:
    arr = list(arr)  # Create a copy of the input list
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr