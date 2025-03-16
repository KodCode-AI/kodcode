from typing import List

def max_triplet_product(arr: List[int]) -> int:
    """
    Finds and returns the maximum product that can be obtained from any three elements in the array.
    """
    if len(arr) < 3:
        raise ValueError("The input array must contain at least three elements.")
    
    arr.sort()
    n = len(arr)
    
    # Product of the three largest elements
    product1 = arr[-1] * arr[-2] * arr[-3]
    
    # Product of the two smallest elements and the largest element
    product2 = arr[0] * arr[1] * arr[-1]
    
    return max(product1, product2)