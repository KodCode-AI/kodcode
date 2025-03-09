class CustomComparator:
    def __init__(self, arr):
        """
        Constructor that initializes the array to be sorted.
        """
        self.arr = arr

    def sort(self):
        """
        Sorts the array according to the rules mentioned:
        - Elements at even indices are sorted in ascending order.
        - Elements at odd indices are sorted in descending order.
        """
        even_indices_sorted = sorted(self.arr[::2])
        odd_indices_sorted_desc = sorted(self.arr[1::2], reverse=True)

        sorted_arr = []
        for i in range(len(self.arr) // 2):
            sorted_arr.append(even_indices_sorted[i])
            if len(self.arr) % 2 == 0 or i < len(self.arr) // 2 - 1:
                sorted_arr.append(odd_indices_sorted_desc[i])

        for i in range(len(self.arr) % 2):
            sorted_arr.append(even_indices_sorted.pop() if i % 2 == 0 else odd_indices_sorted_desc.pop())

        self.arr = sorted_arr

    def getResult(self):
        """
        Returns the sorted array.
        """
        return self.arr


def main():
    arr = [4, 3, 1, 2]
    comparator = CustomComparator(arr)
    comparator.sort()
    print(comparator.getResult())