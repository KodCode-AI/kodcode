def insertion_sort(arr):
    """
    Sorts a list of integers using the insertion sort algorithm.

    Args:
        arr (list): The list of integers to be sorted.

    Returns:
        list: The sorted list of integers.
    """
    # Iterate through each element starting from the second element (index 1)
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted into the sorted portion
        j = i - 1     # Initialize index for the sorted portion

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Shift the element to the right
            j -= 1               # Move to the previous element in the sorted portion

        arr[j + 1] = key  # Insert the key into its correct position

    return arr