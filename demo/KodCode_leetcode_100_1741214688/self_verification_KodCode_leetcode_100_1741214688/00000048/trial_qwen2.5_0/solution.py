def minCompletionTime(jobs):
    """
    Returns the minimum time required to complete all jobs.
    """
    total_time = 0
    current_time = 0
    
    for start, end, cpuTime in jobs:
        current_time = max(current_time, start)  # Wait if the current job starts after the previous one ended.
        total_time += cpuTime  # Add the CPU time of the current job to the total time.
        current_time = end  # Move to the end time of the current job.
    
    return total_time