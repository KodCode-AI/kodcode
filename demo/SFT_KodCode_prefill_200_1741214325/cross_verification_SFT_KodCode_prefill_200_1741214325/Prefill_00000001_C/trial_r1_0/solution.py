from typing import List

def selection_sort(arr: List[int]) -> List[int]:
    sorted_arr = list(arr)
    for i in range(len(sorted_arr)):
        min_pos = i
        for j in range(i + 1, len(sorted_arr)):
            if sorted_arr[j] < sorted_arr[min_pos]:
                min_pos = j
        # Swap the found minimum element to the current position
        sorted_arr[i], sorted_arr[min_pos] = sorted_arr[min_pos], sorted_arr[i]
    return sorted_arr