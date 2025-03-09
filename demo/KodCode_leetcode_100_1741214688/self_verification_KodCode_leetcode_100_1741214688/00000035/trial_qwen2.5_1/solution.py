import math
from typing import List

def max_possible_gcd(nums: List[int], k: int) -> int:
    """
    Returns the maximum GCD after incrementing elements of nums exactly k times.
    """
    max_element = max(nums)
    min_gcd = max_element
    for i in range(max_element):
        current_gcd = 1
        for num in nums:
            if i + num * (k + 1) > 0:
                current_gcd = math.gcd(current_gcd, i + num * (k + 1))
        min_gcd = max(min_gcd, current_gcd)
    return min_gcd