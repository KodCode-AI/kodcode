def insertion_sort(arr):
    """
    Sorts a list of integers in ascending order using the insertion sort algorithm.
    
    The insertion sort algorithm works by iterating through each element of the list 
    and inserting it into its correct position within the previously sorted portion 
    of the list.
    
    Args:
        arr (list): A list of integers to be sorted.
    """
    
    # Iterate through each element in the list starting from the second element
    for i in range(1, len(arr)):
        # Store the current element to be compared with the elements in the sorted portion
        key = arr[i]
        
        # Initialize j to the index before the current element
        j = i - 1
        
        # Shift elements greater than the key to the right to make space for the key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift the element to the right
            j -= 1  # Move to the previous element
        
        # Insert the key into its correct position
        arr[j + 1] = key
    
    # Return the sorted list (in-place sorting, so returning is optional)
    return arr

# Example usage:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", arr)
    insertion_sort(arr)
    print("Sorted list:", arr)