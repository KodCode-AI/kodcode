import numpy as np

class Matrix:
    def __init__(self, *args):
        if isinstance(args[0], (int, float)):
            # Initialize a single value matrix
            self.data = np.array([args])
        elif isinstance(args[0], list):
            # Initialize from list
            self.data = np.array(args)
        else:
            raise ValueError("Invalid initialization arguments")

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def shape(self):
        return self.data.shape

    def __neg__(self):
        return Matrix(-self.data)

    def __mul__(self, another):
        if not isinstance(another, Matrix) or self.shape()[1] != another.shape()[0]:
            raise ValueError("Matrix dimensions mismatch for multiplication")
        return Matrix(np.dot(self.data, another.data))

    def __rmul__(self, other):
        return self * other

    def is_invertible(self) -> bool:
        try:
            np.linalg.inv(self.data)
            return True
        except np.linalg.LinAlgError:
            return False

    def sherman_morrison(self, u: Matrix, v: Matrix) -> 'Matrix':
        if not self.is_invertible():
            return None
        return self.inverse() + (u * (1 / (1 - u @ self @ v)) * v.T)

    def inverse(self) -> 'Matrix':
        return Matrix(np.linalg.inv(self.data))

    def multiply_optimized(self, another: 'Matrix') -> 'Matrix':
        from scipy.linalg import block_tridiagonal
        if not isinstance(another, Matrix) or self.shape()[1] != another.shape()[0]:
            raise ValueError("Matrix dimensions mismatch for multiplication")
        n, m, p = self.shape()[0], self.shape()[1], another.shape()[1]
        blocks = [self[i:i+n, :m] @ another[:, j:j+p] for i in range(0, n, m) for j in range(0, p, m)]
        return Matrix(block_tridiagonal(*blocks, format='csc'))