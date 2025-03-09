def insertion_sort(arr):
    """
    Perform insertion sort on a list of integers.
    
    Parameters:
    arr (list): The list of integers to be sorted.
    
    Returns:
    list: The sorted list of integers.
    
    Explanation:
    1. Iterate over the array starting from the second element (index 1).
    2. For each element, compare it with the elements before it to place it in the correct position.
    3. If the current element is smaller than the previous element, swap them.
    4. Continue this process until the current element is in the correct sorted position.
    5. Repeat the process for all elements in the array.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr