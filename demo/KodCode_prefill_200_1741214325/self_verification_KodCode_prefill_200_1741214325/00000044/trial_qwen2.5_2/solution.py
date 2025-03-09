def binomial_coefficient(n, k):
    """
    Calculate the binomial coefficient (n choose k).
    """
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)