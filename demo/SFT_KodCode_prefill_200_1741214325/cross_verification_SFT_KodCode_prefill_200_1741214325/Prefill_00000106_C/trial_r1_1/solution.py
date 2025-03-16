from typing import List

def insertion_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers using the insertion sort algorithm.
    
    This algorithm iterates through the list, and for each element, it finds the correct
    position within the sorted portion of the list and inserts it there. The algorithm
    keeps growing the sorted portion of the list until the entire list is sorted.
    
    Args:
        arr (list of int): The list of integers to sort.
    
    Returns:
        list of int: The sorted list of integers.
    """
    sorted_arr = arr.copy()
    for i in range(1, len(sorted_arr)):
        current = sorted_arr[i]
        j = i - 1
        while j >= 0 and current < sorted_arr[j]:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1
        sorted_arr[j + 1] = current
    return sorted_arr