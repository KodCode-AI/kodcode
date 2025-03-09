def binomial_coefficient(n, k):
    """
    Calculate the binomial coefficient C(n, k) using a recursive approach.
    """
    # Base cases
    if k == 0 or k == n:
        return 1
    # Recursive case
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)