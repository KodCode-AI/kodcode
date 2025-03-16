def filter_even_numbers(numbers: list[int]) -> list[int]:
    """
    Returns a new list containing only the odd numbers from the input list.
    """
    return [num for num in numbers if num % 2 != 0]