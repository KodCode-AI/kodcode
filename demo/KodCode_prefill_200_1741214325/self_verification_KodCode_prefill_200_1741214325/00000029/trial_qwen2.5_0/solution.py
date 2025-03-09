def bubble_sort(arr):
    """
    Sorts an array using the bubble sort algorithm.
    
    Parameters:
    arr (list): The list of elements to be sorted.
    
    Returns:
    list: The sorted list.
    """
    n = len(arr)
    for i in range(n):
        # Create a flag that will allow the function to terminate early if there's nothing left to sort
        already_sorted = True
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                already_sorted = False
        # If there were no swaps during the last iteration, the array is already sorted, and we can terminate
        if already_sorted:
            break
    return arr