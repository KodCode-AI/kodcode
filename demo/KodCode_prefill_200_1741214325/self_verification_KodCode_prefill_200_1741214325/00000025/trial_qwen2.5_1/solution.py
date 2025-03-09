def max_sum_subarray(arr, k):
    """
    Finds the maximum sum of any subarray of size k within the input array.
    
    Parameters:
    arr (list): The input array of integers.
    k (int): The size of the subarray.
    
    Returns:
    int: The maximum sum of a subarray of size k.
    """
    if not arr or k <= 0 or k > len(arr):
        return None
    
    max_sum = window_sum = sum(arr[:k])
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum