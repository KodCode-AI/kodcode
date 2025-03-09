def bubble_sort(arr):
    """
    Sorts a list of integers using the Bubble Sort algorithm.
    
    Parameters:
    arr (list of int): The list of integers to be sorted.
    
    Returns:
    list of int: The sorted list of integers.
    """
    n = len(arr)
    for i in range(n):
        # Create a flag that will allow the function to terminate early if there's nothing left to sort
        already_sorted = True
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Since we had to swap two elements, we set the flag to True so the algorithm doesn't finish prematurely
                already_sorted = False
        # If there were no swaps during the last iteration, the array is already sorted, and we can terminate
        if already_sorted:
            break
    return arr