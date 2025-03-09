def quick_sort(arr):
    """
    Sorts an array using the Quick Sort algorithm.
    
    Quick Sort is a divide-and-conquer algorithm. It works by selecting a 'pivot'
    element from the array and partitioning the other elements into two sub-arrays,
    according to whether they are less than or greater than the pivot. The sub-arrays
    are then sorted recursively.
    
    Parameters:
    arr (list): The list of elements to be sorted.
    
    Returns:
    list: The sorted list.
    """
    
    # Base case: if the array is empty or contains a single element, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose a pivot (here we choose the last element)
    pivot = arr[-1]
    
    # Partition the array into three lists: less than, equal to, and greater than the pivot
    less = [x for x in arr[:-1] if x < pivot]
    greater = [x for x in arr[:-1] if x > pivot]
    equal = [x for x in arr if x == pivot]
    
    # Recursively apply quick_sort to the less and greater lists and combine the results
    return quick_sort(less) + equal + quick_sort(greater)