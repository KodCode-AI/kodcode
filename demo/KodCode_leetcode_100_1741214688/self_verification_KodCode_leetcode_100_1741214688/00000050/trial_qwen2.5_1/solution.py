def count_ways_to_sum_consecutively(n):
    """
    Given an integer n, returns the number of ways to represent n as a sum of consecutive positive integers.
    """
    total_ways = 0
    start = 1
    current_sum = 0
    
    while start <= n // 2:
        current_sum += start
        start += 1
        
        while current_sum > n:
            current_sum -= start - 1
            start -= 1
        
        if current_sum == n:
            total_ways += 1
    
    return total_ways