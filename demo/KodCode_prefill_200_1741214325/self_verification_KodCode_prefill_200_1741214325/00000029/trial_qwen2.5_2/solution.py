def bubble_sort(arr):
    """
    Sorts a list of numbers using the bubble sort algorithm.
    
    Parameters:
    arr (list): The list of numbers to be sorted.
    
    Returns:
    list: The sorted list.
    """
    n = len(arr)
    for i in range(n):
        # Create a flag that will allow the function to terminate early if there's nothing left to sort
        swapped = False
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no elements were swapped by inner loop, then break
        if not swapped:
            break
    return arr