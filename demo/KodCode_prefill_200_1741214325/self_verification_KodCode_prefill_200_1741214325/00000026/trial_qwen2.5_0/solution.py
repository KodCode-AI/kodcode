def factorial(n):
    """
    Calculates the factorial of a number using recursion.
    :param n: Integer, the number to calculate the factorial for.
    :return: Integer, the factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)