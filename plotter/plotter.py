import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, lattice):
        self.lattice = lattice
        self.plt = plt
        self.plt.figure(figsize=(8, 8))
        self.plt.title('Lattice')
        self.get_basic_2D_axis(step_range=range(-10, 11, 1))

    def get_basic_2D_axis(self, step_range):
        self.plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')
        self.plt.axhline(0, color='black', linewidth=0.5)
        self.plt.axvline(0, color='black', linewidth=0.5)
        self.plt.xticks(step_range)
        self.plt.yticks(step_range)
        self.plt.xlabel('X')
        self.plt.ylabel('Y')

    def plot_lattice(self):
        for element in self.lattice.spanned_elements:
            if abs(element[0]) > 10 or abs(element[1]) > 10:
                continue
            self.plt.plot(element[0], element[1], 'go')
            if element in self.lattice.basis.elements:
                self.plt.plot(element[0], element[1], 'ro')

    def get_plt(self):
        return self.plt
