from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    sorted_arr = arr[:]  # Make a copy of the original array to avoid modifying it
    n = len(sorted_arr)
    
    for i in range(n):
        swapped = False  # Flag to check if any swap occurred in the current pass
        
        # We need to compare each element with the next one up to (n - i - 1) times
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                # Swap the elements
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        
        # If no swaps were made in the current pass, the array is already sorted
        if not swapped:
            break
    
    return sorted_arr