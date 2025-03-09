def find_median(numbers):
    """
    Returns the median of a list of numbers.
    If the list has an odd number of elements, the median is the middle element.
    If the list has an even number of elements, the median is the average of the two middle elements.
    """
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]