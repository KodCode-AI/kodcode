def find_second_largest(numbers):
    """
    Returns the second largest number in the list `numbers`.
    If the list has less than 2 unique numbers, it returns None.
    """
    if len(numbers) < 2:
        return None
    
    # Find the largest and second largest numbers
    first, second = float('-inf'), float('-inf')
    for num in numbers:
        if num > first:
            first, second = num, first
        elif first > num > second:
            second = num
            
    # Check if the second largest is still the same as the largest (in case of duplicates)
    if second == float('-inf'):
        return None
    return second