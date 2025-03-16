def max_triplet_product(arr):
    if len(arr) < 3:
        return None  # Assuming the function is called with arr having at least three elements
    arr.sort()
    candidate1 = arr[-1] * arr[-2] * arr[-3]
    candidate2 = arr[0] * arr[1] * arr[-1]
    return max(candidate1, candidate2)