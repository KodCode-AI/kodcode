def max_sum_subarray(arr, k):
    """
    Returns the maximum sum of any subarray of size k from the input array.
    :param arr: List[int] -- input array of integers
    :param k: int -- size of the subarray
    :return: int -- maximum sum of a subarray of size k
    """
    if not arr or k <= 0 or k > len(arr):
        return None
    max_sum = window_sum = sum(arr[:k])
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    return max_sum