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
        # self.minkowski_first_theorem_distance = self.basis.minkowski_first_theorem_distance()

    def span(self):
        # find range for x
        x_pointer = min(self.basis.elements, key=lambda x: abs(x[0]) if abs(x[0]) != 0 else float('inf'))
        y_pointer = min(self.basis.elements, key=lambda x: abs(x[1]) if abs(x[1]) != 0 else float('inf'))
        z_x_r = 0
        while scalar_prod(z_x_r, x_pointer)[0] < 10:
            z_x_r += 1
        print(z_x_r)
        z_x_l = 0
        while scalar_prod(z_x_l, x_pointer)[0] > -10:
            z_x_l -= 1
        z_y_r = 0
        while scalar_prod(z_y_r, y_pointer)[1] < 10:
            z_y_r += 1
        z_y_l = 0
        while scalar_prod(z_y_l, y_pointer)[1] > -10:
            z_y_l -= 1
        z_r = max(z_x_r, z_y_r)
        z_l = min(z_x_l, z_y_l)

        self.spanned_elements.extend(self.basis.elements)
        for z1 in range(z_l, z_r + 1):
            for z2 in range(z_l, z_r + 1):
                v = add_vectors(scalar_prod(z1, self.basis.elements[0]), scalar_prod(z2, self.basis.elements[1]))
                self.spanned_elements.append(v)


if __name__ == '__main__':
    basis = Matrix(elements=[[1, 1], [-2, 1]])
    lattice = Lattice(basis)
    plotter = Plotter(lattice=lattice)
    window = Window(plotter=plotter)
    window.open()
