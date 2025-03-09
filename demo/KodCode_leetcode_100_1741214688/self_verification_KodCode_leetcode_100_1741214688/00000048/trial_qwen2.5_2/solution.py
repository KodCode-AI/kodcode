def minCompletionTime(jobs):
    """
    Calculates the minimum time required to complete all jobs.
    """
    total_time = 0
    current_time = 0
    for start, end, cpu_time in jobs:
        current_time = max(current_time, start) + cpu_time
        total_time = current_time
    return total_time