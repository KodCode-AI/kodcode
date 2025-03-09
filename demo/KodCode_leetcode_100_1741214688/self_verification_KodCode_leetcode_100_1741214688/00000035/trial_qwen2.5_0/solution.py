import math
from typing import List

def maximize_gcd(nums: List[int], k: int) -> int:
    """
    Returns the maximum possible GCD of the array nums after performing exactly k operations.
    """
    max_val = max(nums)
    min_val = min(nums)
    possible_gcds = set()
    
    for i in range(min_val, max_val // 2 + 1):
        if max_val % i == 0:
            possible_gcds.add(i)
    
    for gcd in possible_gcds:
        if all((num + (k * (num % gcd == 0))) % gcd == 0 for num in nums):
            return gcd
    
    return 1