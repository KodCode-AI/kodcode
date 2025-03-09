def max_product_of_triplet(arr):
    """
    Returns the maximum product that can be obtained by multiplying any three elements from the array.
    """
    arr.sort()
    n = len(arr)
    # The maximum product can be either (the product of the three largest numbers) 
    # or (the product of the two smallest numbers (which could be negative) and the largest number).
    return max(arr[0] * arr[1] * arr[n-1], arr[n-3] * arr[n-2] * arr[n-1])