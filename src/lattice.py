import math

from plotter.plotter import Plotter
from plotter.window import Window
from src.matrix import Matrix
from src.vector_utils import scalar_prod, add_vectors


class Lattice:
    def __init__(self, basis: Matrix):
        self.dimension = basis.rows_num
        self.basis = basis
        self.spanned_elements = []
        self.span()
        self.minkowski_first_theorem_distance = self.get_minkowski_first_theorem_distance()

    def span(self):
        self.spanned_elements = []
        # find range for x and y
        x_pointer = min(self.basis.elements, key=lambda x: abs(x[0]) if abs(x[0]) != 0 else float('inf'))
        y_pointer = min(self.basis.elements, key=lambda x: abs(x[1]) if abs(x[1]) != 0 else float('inf'))
        x_pointer_x = abs(x_pointer[0])
        y_pointer_y = abs(y_pointer[1])
        z_x = int(10 / x_pointer_x)
        z_y = int(10 / y_pointer_y)
        z_range = max(3*max(z_x, z_y), 30)
        self.spanned_elements.extend(self.basis.elements)
        for z1 in range(-z_range, z_range + 1):
            for z2 in range(-z_range, z_range + 1):
                v = add_vectors(scalar_prod(z1, self.basis.elements[0]), scalar_prod(z2, self.basis.elements[1]))
                self.spanned_elements.append(v)

    def refresh_lattice(self):
        self.span()
        self.minkowski_first_theorem_distance = self.get_minkowski_first_theorem_distance()

    def get_minkowski_first_theorem_distance(self):
        return math.sqrt(self.dimension) * abs(self.basis.get_determinant()) ** (1 / self.dimension)


if __name__ == '__main__':
    basis = Matrix(elements=[[-5, 1], [2, -2]])
    lattice = Lattice(basis)
    lattice.span()
    plotter = Plotter(lattice=lattice)
    plotter.plot_lattice()
    plotter.show()
    window = Window(plotter=plotter)
