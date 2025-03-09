def max_team_product(speed, efficiency, k):
    """
    Returns the maximum possible product of the team's average speed and the minimum efficiency.
    """
    from heapq import nlargest
    
    # Create a list of tuples (efficiency, speed) and sort it by efficiency in descending order.
    engineers = sorted(zip(efficiency, speed), reverse=True)
    sum_speed = 0
    max_heap = []
    max_product = 0
    
    for eff, spd in engineers:
        if len(max_heap) < k:
            sum_speed += spd
            nlargest(max_heap, eff)
        else:
            sum_speed += spd
            sum_speed -= heappushpop(max_heap, eff)
        
        if len(max_heap) == k:
            max_product = max(max_product, eff * (sum_speed // k))
    
    return max_product % (10**9 + 7)