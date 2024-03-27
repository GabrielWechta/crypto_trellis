import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, lattice):
        self.lattice = lattice
        self.fig, self.ax = plt.subplots()
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

    def plot_lattice(self):
        for element in self.lattice.spanned_elements:
            if abs(element[0]) > 10 or abs(element[1]) > 10:
                continue
            self.ax.plot(element[0], element[1], 'go')
            if element in self.lattice.basis.elements:
                self.ax.plot(element[0], element[1], 'ro')

    def refresh_ax(self):
        self.ax.clear()
        self.init_basic_2D_axis()

    def show(self):
        plt.show()

    def get_fig_ax(self):
        return self.fig, self.ax
