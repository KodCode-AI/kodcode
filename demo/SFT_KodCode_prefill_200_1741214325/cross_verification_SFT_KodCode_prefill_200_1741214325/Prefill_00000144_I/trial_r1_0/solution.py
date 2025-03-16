def max_triplet_product(arr):
    arr.sort()
    candidate1 = arr[-1] * arr[-2] * arr[-3]
    candidate2 = arr[0] * arr[1] * arr[-1]
    return max(candidate1, candidate2)