class CustomComparator:
    def __init__(self, arr):
        """
        Initializes the array to be sorted.
        """
        self.arr = arr[:]

    def sort(self):
        """
        Sorts the array according to the rules:
        - Elements at even indices are sorted in ascending order.
        - Elements at odd indices are sorted in descending order.
        """
        even_indices = sorted([self.arr[i] for i in range(0, len(self.arr), 2)])
        odd_indices = sorted([self.arr[i] for i in range(1, len(self.arr), 2)], reverse=True)
        
        sorted_arr = []
        for i in range(len(self.arr)):
            if i % 2 == 0:
                sorted_arr.append(even_indices.pop(0))
            else:
                sorted_arr.append(odd_indices.pop(0))
        
        self.arr = sorted_arr

    def get_result(self):
        """
        Returns the sorted array.
        """
        return self.arr


def main():
    comparator = CustomComparator([10, 11, 12, 13, 14, 15, 16, 17])
    comparator.sort()
    print(comparator.get_result())  # Expected output: [10, 17, 12, 15, 14, 13, 16, 11]


if __name__ == "__main__":
    main()