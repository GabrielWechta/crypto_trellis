import tkinter as tk
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Window:
    def __init__(self, plotter):
        self.plotter = plotter
        self.root = tk.Tk()
        self.canvas = None
        self.sliders = []
        self.plotting_arguments = {"minkowski": False, "orthogonal_basis": False, "fundamental_region": False}
        self.plotting_arguments_functions = {
            "minkowski": self.change_plot_arg_minkowski,
            "orthogonal_basis": self.change_plot_arg_orthogonal_basis,
            "fundamental_region": self.change_plot_arg_fundamental_region
        }
        self.init_basic_window()

    def refresh_lattice_plot(self):
        self.plotter.refresh_ax()
        self.plotter.plot_lattice(self.plotting_arguments)
        self.canvas.draw()

    def init_basic_window(self):
        self.root.title("Slider and Plot")
        frame = ttk.Frame(self.root, padding="100")
        frame.grid(row=0, column=0)
        for i in range(4):
            if i % 2 == 0:
                slider_label = ttk.Label(frame, text=f"b_{i // 2}")
                slider = tk.Scale(frame, from_=-100, to=101, tickinterval=2, orient=tk.HORIZONTAL, length=300,
                                  command=lambda value, idx=i: self.update_plot(idx))
                slider.grid(row=i // 2, column=0)
            else:
                slider_label = ttk.Label(frame, text=f"b_{i // 2}")
                slider = tk.Scale(frame, from_=100, to=-101, tickinterval=2, orient=tk.VERTICAL, length=300,
                                  command=lambda value, idx=i: self.update_plot(idx))
                slider.grid(row=i // 2, column=1)
            slider_label.grid(row=i // 2, column=0, sticky=tk.N)
            slider.bind("<ButtonRelease-1>", lambda event, idx=i: self.update_plot(idx))
            self.sliders.append(slider)

        # Create the inner frame
        inner_frame = tk.Frame(frame, bg="darkgrey", padx=50, pady=50)
        inner_frame.grid(row=2, column=0, rowspan=2)
        for i, plot_arg in enumerate(self.plotting_arguments):
            button = ttk.Button(inner_frame, text=plot_arg, command=self.plotting_arguments_functions[plot_arg])
            button.pack(side=tk.LEFT, padx=10, pady=10)

        self.canvas = FigureCanvasTkAgg(self.plotter.fig, master=frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=2, rowspan=4)
        self.update_plot()
        self.root.mainloop()

    def update_plot(self, slider_idx=None):
        if slider_idx is None:
            return
        value = float(self.sliders[slider_idx].get()) / 10
        self.plotter.refresh_ax()
        match slider_idx:
            case 0:
                self.plotter.lattice.basis.elements[0][0] = value
            case 1:
                self.plotter.lattice.basis.elements[0][1] = value
            case 2:
                self.plotter.lattice.basis.elements[1][0] = value
            case 3:
                self.plotter.lattice.basis.elements[1][1] = value

        self.plotter.lattice.refresh_lattice()
        self.refresh_lattice_plot()

    def change_plot_arg_minkowski(self):
        self.plotting_arguments["minkowski"] = not self.plotting_arguments["minkowski"]
        self.refresh_lattice_plot()

    def change_plot_arg_orthogonal_basis(self):
        self.plotting_arguments["orthogonal_basis"] = not self.plotting_arguments["orthogonal_basis"]
        self.refresh_lattice_plot()

    def change_plot_arg_fundamental_region(self):
        self.plotting_arguments["fundamental_region"] = not self.plotting_arguments["fundamental_region"]
        self.refresh_lattice_plot()


if __name__ == '__main__':
    window = Window(None)
