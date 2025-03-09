from typing import List
from math import gcd
from functools import reduce

def maxGCD(nums: List[int], k: int) -> int:
    """
    Increments an element in nums exactly k times to maximize the GCD of the array.
    """
    # The optimal strategy is to maximize the GCD by making all elements the same
    # Since we can increment any element any number of times, we can aim to make all elements equal.
    # After k increments, we can achieve a maximum GCD by choosing the smallest element as the target value.
    # Incrementing the smallest elements will ensure the GCD is maximized.
    current_gcd = 0
    min_num = min(nums)
    for _ in range(k):
        # Since we are incrementing the smallest number, the GCD is likely to increase
        # Keeping track of the GCD as we increment the smallest element
        current_gcd = gcd(current_gcd, min_num)
        min_num += 1
    return current_gcd