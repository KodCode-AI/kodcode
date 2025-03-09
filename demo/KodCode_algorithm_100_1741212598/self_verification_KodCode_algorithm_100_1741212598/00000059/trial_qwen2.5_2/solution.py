def custom_selection_sort(arr):
    """
    Returns a new list where all even numbers are sorted in ascending order,
    while odd numbers remain in their original positions.
    """
    # Extract the even numbers and sort them
    even_numbers = sorted([num for num in arr if num % 2 == 0])
    even_index = 0
    
    # Replace the even numbers in their original positions with the sorted ones
    return [even_numbers[even_index] if num % 2 == 0 else num for index, num in enumerate(arr)]