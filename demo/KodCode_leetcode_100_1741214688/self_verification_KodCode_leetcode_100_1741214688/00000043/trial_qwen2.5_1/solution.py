from typing import List
from heapq import nsmallest

def max_product(speed: List[int], efficiency: List[int], k: int) -> int:
    """
    Calculate the maximum product of the average speed and the minimum efficiency.
    """
    mod = 10**9 + 7
    n = len(speed)
    engineers = sorted(zip(efficiency, speed), reverse=True)
    total_speed = 0
    max_product = 0
    
    for e, s in engineers:
        if k == 1:
            max_product = max(max_product, (total_speed + s) * e)
        else:
            k -= 1
            total_speed += s
            max_product = max(max_product, (total_speed / k) * e)
    
    return max_product % mod