import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

from src.vector_utils import scalar_prod


class Plotter:
    def __init__(self, lattice):
        self.lattice = lattice
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        # self.fig.title('Lattice')
        self.init_basic_2D_axis(step_range=range(-10, 11, 1))

    def init_basic_2D_axis(self, step_range=range(-10, 11, 1)):
        self.ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')
        self.ax.axhline(0, color='black', linewidth=0.5)
        self.ax.axvline(0, color='black', linewidth=0.5)
        self.ax.set_xticks(step_range)
        self.ax.set_yticks(step_range)
        self.ax.set_xlim(step_range[0], step_range[-1])
        self.ax.set_ylim(step_range[0], step_range[-1])
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')

    def plot_lattice(self, plotting_arguments=None):
        for element in self.lattice.spanned_elements:
            if abs(element[0]) > 10 or abs(element[1]) > 10:
                continue
            self.ax.plot(element[0], element[1], 'bo')
            if element in self.lattice.basis.elements:
                self.ax.plot(element[0], element[1], 'ro')

        if plotting_arguments is None:
            return
        # Minkowski first theorem distance
        if plotting_arguments['minkowski']:
            self.plot_minkowski_distance()
        # Orthogonal basis
        if plotting_arguments['orthogonal_basis']:
            self.plot_orthogonal_basis()
        # Fundamental region
        if plotting_arguments['fundamental_region']:
            self.plot_fundamental_region()

    def plot_minkowski_distance(self):
        radius = self.lattice.get_minkowski_first_theorem_distance()
        minkowski_dist_circle = plt.Circle((0, 0), radius, alpha=0.25, color='yellow')
        self.ax.add_artist(minkowski_dist_circle)

    def plot_orthogonal_basis(self):
        orthogonal_basis = self.lattice.basis.deepcopy()
        orthogonal_basis.gram_schmidt_orthogonalization()
        for element in orthogonal_basis.elements:
            self.ax.arrow(0, 0, element[0], element[1], head_width=0.3, head_length=0.3, fc='g', ec='g')

    def plot_fundamental_region(self):
        orthogonal_basis = self.lattice.basis.deepcopy()
        orthogonal_basis.gram_schmidt_orthogonalization()
        ov0 = scalar_prod(1 / 2, orthogonal_basis.elements[0])
        ov1 = scalar_prod(1 / 2, orthogonal_basis.elements[1])
        for e in self.lattice.spanned_elements:
            if abs(e[0]) > 15 or abs(e[1]) > 15:
                continue
            parallelogram = Polygon([
                (e[0] - ov0[0] - ov1[0], e[1] - ov0[1] - ov1[1]),
                (e[0] + ov0[0] - ov1[0], e[1] + ov0[1] - ov1[1]),
                (e[0] + ov0[0] + ov1[0], e[1] + ov0[1] + ov1[1]),
                (e[0] - ov0[0] + ov1[0], e[1] - ov0[1] + ov1[1]),
            ], closed=True,
                fill=None, edgecolor='b')
            self.ax.add_patch(parallelogram)

    # def plot_fundamental_region(self):
    #     for element in self.lattice.spanned_elements:
    #
    #     parallelogram = Polygon( [(1, 1), (1, 2), (7, 5), (4, 7)], closed=True, fill=None, edgecolor='b')
    #     self.ax.add_patch(parallelogram)

    def refresh_ax(self):
        self.ax.clear()
        self.init_basic_2D_axis()

    def show(self):
        plt.show()

    def get_fig_ax(self):
        return self.fig, self.ax
