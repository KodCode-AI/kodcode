def max_triplet_product(arr):
    """
    Finds and returns the maximum product that can be obtained from any three elements in the array.
    """
    if len(arr) < 3:
        raise ValueError("The input array must contain at least three elements.")

    # Sort the array to make it easier to find the maximum product
    arr.sort()

    # The maximum product can be either:
    # 1. The product of the three largest numbers
    # 2. The product of the two smallest (potentially negative) numbers and the largest number
    n = len(arr)
    return max(arr[0] * arr[1] * arr[n-1], arr[n-3] * arr[n-2] * arr[n-1])