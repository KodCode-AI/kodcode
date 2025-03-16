import bisect

def longest_increasing_subsequence(nums):
    tails = []
    for num in nums:
        index = bisect.bisect_left(tails, num)
        if index == len(tails):
            tails.append(num)
        else:
            tails[index] = num
    return len(tails)