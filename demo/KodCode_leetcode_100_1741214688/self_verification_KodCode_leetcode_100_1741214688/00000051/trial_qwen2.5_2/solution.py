class CustomComparator:
    def __init__(self, arr):
        """
        Constructor that initializes the array to be sorted.
        """
        self.arr = arr

    def sort(self):
        """
        Sorts the array according to the rules mentioned.
        """
        even_indices = sorted(self.arr[::2])
        odd_indices = sorted(self.arr[1::2], reverse=True)
        self.arr = [even if i % 2 == 0 else odd for i, (even, odd) in enumerate(zip(even_indices, odd_indices + self.arr[-1:] * (len(self.arr) % 2)))]

    def get_result(self):
        """
        Returns the sorted array.
        """
        return self.arr


def main():
    arr = [4, 1, 3, 2, 6, 5]
    comparator = CustomComparator(arr)
    comparator.sort()
    print(comparator.get_result())