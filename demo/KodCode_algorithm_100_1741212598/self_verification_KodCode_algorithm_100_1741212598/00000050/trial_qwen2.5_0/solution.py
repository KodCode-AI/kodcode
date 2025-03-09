import numpy as np

class Matrix:
    def __init__(self, *args):
        if isinstance(args[0], int):
            n, m = args
            self._matrix = np.zeros((n, m))
        else:
            self._matrix = np.array(args)

    def __getitem__(self, key):
        return self._matrix[key]

    def __setitem__(self, key, value):
        self._matrix[key] = value

    def __mul__(self, another):
        if self.ncols != another.nrows:
            raise ValueError("Matrix dimensions do not match for multiplication.")
        return Matrix(self._matrix.dot(another._matrix))

    def is_invertible(self) -> bool:
        return np.linalg.cond(self._matrix) < 1 / sys.float_info.epsilon

    def sherman_morrison(self, u, v):
        if not self.is_invertible():
            return None
        return self.inv().sherman_morrison(u, v)

    def inv(self):
        return Matrix(np.linalg.inv(self._matrix))

    @property
    def nrows(self):
        return self._matrix.shape[0]

    @property
    def ncols(self):
        return self._matrix.shape[1]

    def multiply_optimized(self, another: 'Matrix') -> 'Matrix':
        result = np.dot(self._matrix, another._matrix)
        return Matrix(result)