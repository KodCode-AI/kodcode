from typing import List

def selection_sort(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        min_index = i
        min_val = arr[i]
        for j in range(i + 1, len(arr)):
            if arr[j] < min_val:
                min_val = arr[j]
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr