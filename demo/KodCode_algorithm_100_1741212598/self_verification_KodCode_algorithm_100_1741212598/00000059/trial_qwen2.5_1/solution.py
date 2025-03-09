def custom_selection_sort(numbers):
    """
    Sorts the even numbers in the list while keeping the odd numbers in their original positions.
    """
    # Extract even numbers and sort them
    even_numbers = [num for num in numbers if num % 2 == 0]
    even_numbers.sort()
    
    # Create a generator to cycle through sorted even numbers
    even_it = iter(even_numbers)
    
    # Construct the result list
    result = [next(even_it) if num % 2 == 0 else num for num in numbers]
    return result