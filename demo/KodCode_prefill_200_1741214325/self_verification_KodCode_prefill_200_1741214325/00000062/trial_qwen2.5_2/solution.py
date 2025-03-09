def second_maximum(numbers):
    """
    Returns the second maximum number in a list of integers.
    If the list does not contain at least two different numbers, returns None.
    """
    if len(numbers) < 2:
        return None
    
    max_num = second_max_num = float('-inf')
    
    for num in numbers:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif max_num > num > second_max_num:
            second_max_num = num
            
    if second_max_num == float('-inf'):
        return None
    return second_max_num