class DynamicArray:
    def __init__(self, nums):
        self.nums = nums
        self.max_sum = [num for num in nums]

    def add(self, index, val):
        self.nums[index] += val
        # Update the max_sum array
        for i in range(index, len(self.nums)):
            self.max_sum[i] = max(self.nums[i], (self.max_sum[i-1] if i > 0 else 0) + self.nums[i])

    def find(self, left, right):
        if left == 0:
            return self.max_sum[right]
        return max(self.max_sum[right] - self.max_sum[left-1], self.nums[left])