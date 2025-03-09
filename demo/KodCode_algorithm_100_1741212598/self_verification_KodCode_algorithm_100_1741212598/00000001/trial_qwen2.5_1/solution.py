from typing import List

def insertion_sort(array: List[int], start: int, end: int):
    """Perform insertion sort on the array between start and end."""
    for i in range(start + 1, end + 1):
        key = array[i]
        j = i - 1
        while j >= start and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

def partition(array: List[int], start: int, end: int) -> int:
    """Partition the array using the last element as the pivot."""
    pivot = array[end]
    i = start - 1
    for j in range(start, end):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[end] = array[end], array[i + 1]
    return i + 1

def intro_sort(array: List[int], start: int, end: int, size_threshold: int, max_depth: int) -> List[int]:
    """
    Sorts the array between indices `start` and `end` (inclusive) using Introspective Sort.
    """
    depth = 0
    while end - start >= size_threshold and depth < max_depth:
        depth += 1
        pivot_index = end
        if end - start + 1 < 16:
            pivot_index = (start + end) // 2
        pivot_index = partition(array, start, end)
        if pivot_index - start < end - pivot_index:
            intro_sort(array, start, pivot_index - 1, size_threshold, max_depth)
            start = pivot_index + 1
        else:
            intro_sort(array, pivot_index + 1, end, size_threshold, max_depth)
            end = pivot_index - 1
    if start < end:
        insertion_sort(array, start, end)
    return array