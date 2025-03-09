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
        # Flag to detect any swap
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap arr[j] and arr[j+1]
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
    return arr