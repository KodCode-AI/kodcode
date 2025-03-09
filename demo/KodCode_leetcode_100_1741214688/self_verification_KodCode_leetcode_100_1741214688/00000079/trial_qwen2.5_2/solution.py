from collections import defaultdict

class RangeFreqQuery:
    def __init__(self, arr):
        """
        Initializes the class with the given array `arr`.
        """
        self.freq_map = defaultdict(list)
        for index, value in enumerate(arr):
            self.freq_map[value].append(index)

    def query(self, left, right, value):
        """
        Returns the frequency of the value `value` in the subarray `arr[left...right]`.
        """
        indices = self.freq_map[value]
        if not indices:
            return 0
        left_index = self.bisect_left(indices, left)
        right_index = self.bisect_right(indices, right)
        return right_index - left_index

    def bisect_left(self, arr, target):
        """
        Returns the leftmost index to insert `target` in `arr` to maintain sorted order.
        """
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def bisect_right(self, arr, target):
        """
        Returns the rightmost index to insert `target` in `arr` to maintain sorted order.
        """
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if target < arr[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo