def second_maximum(numbers):
    """
    Returns the second maximum number in the list. If there are not at least two different numbers, returns None.
    """
    if len(numbers) < 2:
        return None
    
    first_max = second_max = float('-inf')
    
    for num in numbers:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif first_max > num > second_max:
            second_max = num
            
    return second_max if second_max != float('-inf') else None