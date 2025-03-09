def insertion_sort(arr):
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
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        
        # Store the current element
        current_value = arr[i]
        
        # Initialize the position where the current element needs to be inserted
        position = i
        
        # Move elements of arr[0..i-1], that are greater than current_value,
        # to one position ahead of their current position
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1
        
        # Insert the current element into its correct position
        arr[position] = current_value
    
    return arr