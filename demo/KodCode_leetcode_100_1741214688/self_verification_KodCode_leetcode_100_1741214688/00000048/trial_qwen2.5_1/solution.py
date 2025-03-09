def minCompletionTime(jobs):
    """
    Returns the minimum time required to complete all jobs in the given order.
    """
    if not jobs:
        return 0

    total_time = 0
    current_time = jobs[0][0]  # Start time of the first job
    
    for start, end, cpu_time in jobs:
        if start > current_time:
            total_time += start - current_time
        total_time += cpu_time
        current_time = end

    return total_time