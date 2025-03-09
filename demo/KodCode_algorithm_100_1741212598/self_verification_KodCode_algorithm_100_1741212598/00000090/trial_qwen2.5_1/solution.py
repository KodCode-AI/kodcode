def calculate_difference(n):
    """
    Calculates the difference between the square of the sum and the sum of the squares of the first n natural numbers.
    """
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
    square_of_sum = (n * (n + 1) // 2) ** 2
    return square_of_sum - sum_of_squares