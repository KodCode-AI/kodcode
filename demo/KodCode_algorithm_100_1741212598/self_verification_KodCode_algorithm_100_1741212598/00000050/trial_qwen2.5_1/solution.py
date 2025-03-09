import numpy as np

class Matrix:
    def __init__(self, rows: int, cols: int, *args):
        self.rows = rows
        self.cols = cols
        if args:
            data = np.array(args).reshape(rows, cols)
            self.data = data.copy()
        else:
            self.data = np.zeros((rows, cols))

    def __getitem__(self, key):
        row, col = key
        return self.data[row, col]

    def __setitem__(self, key, value):
        row, col = key
        self.data[row, col] = value

    def __mul__(self, another):
        if self.cols != another.rows:
            raise ValueError("Dimension mismatch for matrix multiplication.")
        result = Matrix(self.rows, another.cols)
        for i in range(self.rows):
            for j in range(another.cols):
                for k in range(self.cols):
                    result[i, j] += self[i, k] * another[k, j]
        return result

    def multiply_optimized(self, another):
        if self.cols != another.rows:
            raise ValueError("Dimension mismatch for matrix multiplication.")
        result = np.dot(self.data, another.data)
        return Matrix(self.rows, another.cols, *result.flatten())

    def sherman_morrison(self, u, v):
        # Placeholder implementation, actual implementation requires specific conditions
        raise NotImplementedError

    def is_invertible(self) -> bool:
        det = np.linalg.det(self.data)
        return abs(det) > 1e-9  # Assuming machine epsilon as 1e-7 for double precision

# Example usage and checks
a = Matrix(2, 2, 1, 2, 3, 4)
print(a.is_invertible())  # False
b = Matrix(2, 2, 2, -1, -1, 2)
print(b.is_invertible())  # True
c = Matrix(2, 2, 1, 1, 1, 1)
print(c.is_invertible())  # False