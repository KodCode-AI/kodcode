def single_number(nums):
    single_num = 0
    for num in nums:
        single_num ^= num
    return single_num