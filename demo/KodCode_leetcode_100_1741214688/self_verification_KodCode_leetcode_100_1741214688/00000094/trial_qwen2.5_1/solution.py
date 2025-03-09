class CircularArray:
    def __init__(self, size):
        """
        Initializes the CircularArray with size elements, all set to zero.
        """
        self.size = size
        self.array = [0] * size

    def set(self, index, val):
        """
        Sets the value at the given index to val. If the index is out of bounds, it should wrap around to the beginning or end of the array.
        """
        self.array[index % self.size] = val

    def get(self, index):
        """
        Returns the value at the given index. If the index is out of bounds, it should wrap around to the beginning or end of the array.
        """
        return self.array[index % self.size]

    def increment(self, index, val):
        """
        Increments the value at the given index by val. If the index is out of bounds, it should wrap around to the beginning or end of the array.
        """
        self.set(index, self.get(index) + val)

    def to_string(self):
        """
        Returns a string representation of the CircularArray.
        """
        return '[' + ','.join(map(str, self.array)) + ']'