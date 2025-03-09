def binomial_coefficient(n, k):
    """
    Calculate the binomial coefficient C(n, k).
    
    Args:
    n (int): The total number of items.
    k (int): The number of items to choose.
    
    Returns:
    int: The binomial coefficient.
    """
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)