def quick_sort(arr):
    # Base case: If the array is empty or has one element, it's already sorted.
    if len(arr) <= 1:
        return arr
    
    # Select the last element as the pivot.
    pivot = arr[-1]
    
    # Initialize three lists to partition elements: left (less than pivot), middle (equal), right (greater).
    left = []
    middle = []
    right = []
    
    # Iterate through each element in the array to partition.
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            middle.append(num)
        else:
            right.append(num)
    
    # Recursively apply quick_sort to left and right partitions, then combine with middle.
    return quick_sort(left) + middle + quick_sort(right)