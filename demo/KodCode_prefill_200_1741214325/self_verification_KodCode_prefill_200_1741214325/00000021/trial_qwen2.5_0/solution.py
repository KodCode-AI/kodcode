def sum_of_even_numbers(numbers_list):
    """
    Returns the sum of all even numbers in the given list.
    """
    return sum(num for num in numbers_list if num % 2 == 0)