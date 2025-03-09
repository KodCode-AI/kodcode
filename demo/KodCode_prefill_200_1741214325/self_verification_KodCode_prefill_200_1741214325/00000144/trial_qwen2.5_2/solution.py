def max_product_of_triplet(arr):
    """
    Returns the maximum product of a triplet in the array.
    """
    arr.sort()
    n = len(arr)
    # The maximum product can be either:
    # 1. Product of the three largest numbers
    # 2. Product of the two smallest (which could be negative) and the largest number
    return max(arr[0] * arr[1] * arr[n-1], arr[n-3] * arr[n-2] * arr[n-1])