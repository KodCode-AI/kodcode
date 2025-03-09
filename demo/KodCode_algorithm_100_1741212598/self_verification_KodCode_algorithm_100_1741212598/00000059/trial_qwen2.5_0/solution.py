def custom_selection_sort(arr):
    """
    Returns a new list where all even numbers are sorted in ascending order, 
    while all odd numbers remain in their original positions.
    """
    # Extract the even numbers and sort them
    evens = sorted([x for x in arr if x % 2 == 0])
    
    # Reconstruct the array with sorted evens and original odds
    sorted_arr = []
    evens_index = 0
    for num in arr:
        if num % 2 == 0:
            sorted_arr.append(evens[evens_index])
            evens_index += 1
        else:
            sorted_arr.append(num)
    
    return sorted_arr