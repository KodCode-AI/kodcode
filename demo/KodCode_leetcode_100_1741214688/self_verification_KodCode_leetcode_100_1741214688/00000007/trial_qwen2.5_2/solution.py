from typing import List

class DynamicArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.max_vals = [0] * len(nums)

    def add(self, index: int, val: int) -> None:
        """
        Adds val to nums[index] and updates the max_vals array accordingly.
        """
        self.nums[index] += val
        if index == 0:
            self.max_vals[index] = self.nums[index]
        else:
            self.max_vals[index] = max(self.max_vals[index - 1], self.nums[index])

    def find(self, left: int, right: int) -> int:
        """
        Returns the maximum value in the subarray nums[left...right].
        """
        if left == 0:
            return self.max_vals[right]
        else:
            return max(self.max_vals[right], self.nums[left:right+1])