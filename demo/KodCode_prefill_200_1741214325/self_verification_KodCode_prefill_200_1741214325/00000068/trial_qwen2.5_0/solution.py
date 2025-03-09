def quick_sort(arr):
    """
    Sorts an array using the quick sort algorithm.

    Parameters:
    arr (list): The list to be sorted.

    Returns:
    list: The sorted list.
    """
    # Base case: if the array has 1 or 0 elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Recursive case
    else:
        # Select the pivot element (here, the last element is chosen)
        pivot = arr[-1]
        # Partition the array into two halves based on the pivot
        smaller_elements = [x for x in arr[:-1] if x <= pivot]
        larger_elements = [x for x in arr[:-1] if x > pivot]

        # Recursively sort the smaller and larger arrays, then combine with the pivot
        return quick_sort(smaller_elements) + [pivot] + quick_sort(larger_elements)


Let's break down the code line by line:
1. **Function Definition**: Defines a function named `quick_sort` that takes a list `arr` as its parameter.
2. **Base Case**: Checks if the input array has 1 or 0 elements. If so, it returns the array as it is already sorted.
3. **Recursive Case**: If the array has more than one element, continues to the next steps.
   - **Pivot**: Chooses the last element of the array as the pivot.
   - **Partitioning**: Uses list comprehensions to create two new lists: `smaller_elements` for elements less than or equal to the pivot, and `larger_elements` for elements greater than the pivot.
   - **Recursive Sorting**: Recursively calls `quick_sort` on the `smaller_elements` and `larger_elements`, and combines the results with the pivot in between.
4. **Return**: Returns the sorted list.

The pivot selection and partitioning are crucial steps in implementing the quick sort algorithm, and the recursion progresses until the base case is reached.