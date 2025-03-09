def max_sum_subarray_of_size_k(arr, k):
    """
    Find the maximum sum of any subarray of size k within the input array of integers.
    
    :param arr: List[int] - The input array of integers.
    :param k: int - The size of the subarray.
    :return: int - The maximum sum of any subarray of size k.
    """
    if not arr or k <= 0 or k > len(arr):
        return None
    
    max_sum = window_sum = sum(arr[:k])
    for i in range(len(arr) - k):
        window_sum += arr[i + k] - arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum