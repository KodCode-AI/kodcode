def find_missing_element(nums):
    m = len(nums)
    n = m + 1
    expected = n * (n + 1) // 2
    actual = sum(nums)
    return expected - actual