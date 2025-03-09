def insertion_sort(arr):
    """
    Sorts an array of integers using the insertion sort algorithm.
    
    This algorithm works by iterating over the elements, and for each element, 
    shifting the already sorted elements to the right to make space for the 
    new element and inserting the element in the correct position.
    
    Parameters:
    - arr: List[int], the list of integers to be sorted.
    
    Returns:
    - List[int], the sorted list.
    """
    # Loop through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key, 
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr