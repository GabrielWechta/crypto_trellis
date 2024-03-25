import random
from typing import List

from src.utils import dot_prod


class Matrix:
    def __init__(self, elements: List[List[int | float]] = None, dim: int = None, identity: bool = False):
        if elements is None:
            elements = self.get_random_elements(dim, identity)
        self.assert_correct_params(elements)
        self.elements = elements
        self.rows_num = len(elements)
        self.cols_num = len(elements[0])

    def __add__(self, other):
        assert self.rows_num == other.rows_num and self.cols_num == other.cols_num, "Matrices must have the same size"
        return Matrix(
            [[self.elements[i][j] + other.elements[i][j] for j in range(self.cols_num)] for i in range(self.rows_num)])

    def __sub__(self, other):
        assert self.rows_num == other.rows_num and self.cols_num == other.cols_num, "Matrices must have the same size"
        return Matrix(
            [[self.elements[i][j] - other.elements[i][j] for j in range(self.cols_num)] for i in range(self.rows_num)])

    def __mul__(self, other):
        if isinstance(other, Matrix):
            assert self.cols_num == other.rows_num, "Matrices must have the same size"
            result = [[dot_prod(self.elements[row], [other.elements[i][col] for i in range(other.rows_num)])
                       for col in range(other.cols_num)] for row in range(self.rows_num)]
            return Matrix(elements=result)

        if isinstance(other, (int, float)):
            result = [[other * element for element in row] for row in self.elements]
            return Matrix(elements=result)
        else:
            assert self.cols_num == other.rows_num, "Matrices must have the same size"
            raise NotImplemented("Scalar multiplication is only supported with int or float")

    def __rmul__(self, scalar):
        return self * scalar

    def __str__(self):
        matrix_str = ""
        max_element_len = max(max(len(str(element)) for element in row) for row in self.elements)
        for row in self.elements:
            for element in row:
                if isinstance(element, int):
                    matrix_str += f"{element:>{max_element_len + 1}d}"
                else:
                    matrix_str += f"{element:>{max_element_len + 2}.2f}"
            matrix_str += "\n"
        return matrix_str

    @staticmethod
    def get_random_elements(dim: int, identity: bool):
        if identity is True:
            return [[1 if i == j else 0 for j in range(dim)] for i in range(dim)]
        return [[round(random.uniform(-10, 10), 1) for _ in range(dim)] for _ in range(dim)]

    @staticmethod
    def assert_correct_params(elements: List[List[int]]):
        assert all(len(row) == len(elements[0]) for row in elements), "All rows must have the same length"
        assert all(len(col) == len(elements) for col in zip(*elements)), "All columns must have the same length"
        # assert all(isinstance(el, type(elements[0][0])) for row in elements for el in
        #            row), "All elements must be of the same type"

    def transpose(self):
        return Matrix([[self.elements[j][i] for j in range(self.rows_num)] for i in range(self.cols_num)])

    def get_determinant(self):
        assert self.rows_num == self.cols_num, "Matrix must be square"

        # Base case for 1x1 matrix
        if self.rows_num == 1:
            return self.elements[0][0]
        # Base case for 2x2 matrix
        elif self.rows_num == 2:
            return self.elements[0][0] * self.elements[1][1] - self.elements[0][1] * self.elements[1][0]
        else:
            det = 0
            for j in range(self.cols_num):
                det += self.elements[0][j] * self.cofactor(0, j)
            return det

    def cofactor(self, row, col):
        return (-1) ** (row + col) * self.minor(row, col).get_determinant()

    def minor(self, row, col):
        minor_elements = [
            [self.elements[i][j] for j in range(self.cols_num) if j != col]
            for i in range(self.rows_num) if i != row
        ]
        return Matrix(elements=minor_elements)

    def inverse(self):
        assert self.get_determinant() != 0, "Matrix is not invertible"
        return (1 / self.get_determinant()) * self.adjoint()

    def adjoint(self):
        cofactors = [[self.cofactor(i, j) for j in range(self.cols_num)] for i in range(self.rows_num)]
        return Matrix(elements=cofactors).transpose()

    def to_row_echelon_form(self):
        # TODO fix this
        lead = 0
        row_count = self.rows_num
        col_count = self.cols_num
        for r in range(row_count):
            if lead >= col_count:
                return
            i = r
            while self.elements[i][lead] == 0:
                i += 1
                if i == row_count:
                    i = r
                    lead += 1
                    if col_count == lead:
                        return
            self.elements[i], self.elements[r] = self.elements[r], self.elements[i]

            lv = self.elements[r][lead]
            self.elements[r] = [mrx / lv for mrx in self.elements[r]]

            for i in range(row_count):
                if i != r:
                    lv = self.elements[i][lead]
                    self.elements[i] = [iv - lv * rv for rv, iv in zip(self.elements[r], self.elements[i])]

            lead += 1


if __name__ == "__main__":
    m = Matrix(dim=6, identity=True)
    n = Matrix(dim=6)
    e = m * n
    print(e)
    e.to_row_echelon_form()
    print(e)
    # print(m.get_determinant())
