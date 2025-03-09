def count_good_triangles(nums):
    """
    Returns the number of unique triangles that can be formed from the elements of nums.
    The result is modulo 10^9 + 7.
    """
    MOD = 10**9 + 7
    nums.sort()
    n = len(nums)
    count = 0

    for i in range(n - 2):
        k = i + 2
        for j in range(i + 1, n - 1):
            while k < n and nums[i] + nums[j] > nums[k]:
                k += 1
            count += k - j - 1
            count %= MOD

    return count