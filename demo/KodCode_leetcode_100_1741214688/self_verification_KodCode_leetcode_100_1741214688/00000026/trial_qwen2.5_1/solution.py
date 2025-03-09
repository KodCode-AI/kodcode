def count_triangles(nums):
    """
    Returns the number of unique triangles that can be formed from the elements of nums
    modulo 10^9 + 7.
    """
    mod = 10**9 + 7
    nums.sort()
    count = 0
    n = len(nums)
    
    for i in range(n-2):
        k = i + 2
        for j in range(i+1, n-1):
            while k < n and nums[i] + nums[j] > nums[k]:
                k += 1
            count += max(0, k - j - 1)
    
    return count % mod