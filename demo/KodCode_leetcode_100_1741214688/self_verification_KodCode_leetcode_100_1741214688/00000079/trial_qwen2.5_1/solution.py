from collections import defaultdict

class RangeFreqQuery:
    def __init__(self, arr):
        """
        Initializes the class with the given array `arr`.
        """
        self.frequency = defaultdict(list)
        for idx, value in enumerate(arr):
            self.frequency[value].append(idx)

    def query(self, left, right, value):
        """
        Returns the frequency of the value `value` in the subarray `arr[left...right]`.
        """
        if value not in self.frequency:
            return 0
        indices = self.frequency[value]
        start, end = 0, len(indices) - 1
        while start <= end:
            mid = (start + end) // 2
            if indices[mid] < left:
                start = mid + 1
            else:
                end = mid - 1
        left_idx = start
        if left_idx >= len(indices) or indices[left_idx] > right:
            return 0
        start, end = 0, len(indices) - 1
        while start <= end:
            mid = (start + end) // 2
            if indices[mid] <= right:
                start = mid + 1
            else:
                end = mid - 1
        right_idx = end
        return right_idx - left_idx + 1