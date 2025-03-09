def find_median(numbers):
    """
    Returns the median of a list of numbers.
    If the list has an odd number of elements, returns the middle element.
    If the list has an even number of elements, returns the average of the two middle elements.
    """
    n = len(numbers)
    if n == 0:
        raise ValueError("The list is empty.")
    sorted_numbers = sorted(numbers)
    mid_index = n // 2
    
    if n % 2 == 1:
        return sorted_numbers[mid_index]
    else:
        return (sorted_numbers[mid_index - 1] + sorted_numbers[mid_index]) / 2