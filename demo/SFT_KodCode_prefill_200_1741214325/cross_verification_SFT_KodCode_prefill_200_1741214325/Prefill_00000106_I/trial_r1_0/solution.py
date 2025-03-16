def insertion_sort(arr):
    """
    This function sorts a list of integers using the Insertion Sort algorithm.
    It works by building the sorted list one item at a time by inserting each
    element into its correct position within the sorted portion of the list.
    """
    
    # Loop through the list starting from the second element (index 1)
    for i in range(1, len(arr)):
        # Store the current element to be compared and inserted
        current_value = arr[i]
        
        # Initialize the position for comparison
        j = i - 1
        
        # Compare the current element with elements before it and shift them if necessary
        while j >= 0 and arr[j] > current_value:
            # Shift the element to the right to make space for the current element
            arr[j + 1] = arr[j]
            # Move to the previous element
            j = j - 1
        
        # Insert the current element into its correct position
        arr[j + 1] = current_value
    
    # Return the sorted list
    return arr

# Example usage:
# arr = [64, 34, 25, 12, 22, 11, 90]
# insertion_sort(arr)
# print("Sorted array:", arr)