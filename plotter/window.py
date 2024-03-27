import tkinter as tk
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Window:
    def __init__(self, plotter):
        self.plotter = plotter
        self.root = tk.Tk()
        self.init_basic_window()

    def init_basic_window(self):
        self.root.title("Slider and Plot")
        frame = ttk.Frame(self.root, padding="100")
        frame.grid(row=0, column=0)
        self.sliders = []
        for i in range(4):
            if i % 2 == 0:
                slider_label = ttk.Label(frame, text=f"b_{i//2}")
                slider = tk.Scale(frame, from_=-100, to=101, tickinterval=2, orient=tk.HORIZONTAL, length=300, command=lambda value, idx=i: self.update_plot(idx))
                slider.grid(row=i//2, column=0)
            else:
                slider_label = ttk.Label(frame, text=f"b_{i//2}")
                slider = tk.Scale(frame, from_=100, to=-101, tickinterval=2, orient=tk.VERTICAL, length=300, command=lambda value, idx=i: self.update_plot(idx))
                slider.grid(row=i//2, column=1)
            slider_label.grid(row=i//2, column=0, sticky=tk.N)
            slider.bind("<ButtonRelease-1>", lambda event, idx=i: self.update_plot(idx))
            self.sliders.append(slider)

        self.canvas = FigureCanvasTkAgg(self.plotter.fig, master=frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=2, rowspan=4)
        self.update_plot(-1)
        self.root.mainloop()

    def update_plot(self, slider_idx):
        value = float(self.sliders[slider_idx].get())/10
        self.plotter.refresh_ax()
        match slider_idx:
            case 0: self.plotter.lattice.basis.elements[0][0] = value
            case 1: self.plotter.lattice.basis.elements[0][1] = value
            case 2: self.plotter.lattice.basis.elements[1][0] = value
            case 3: self.plotter.lattice.basis.elements[1][1] = value
            case -1: pass

        self.plotter.lattice.refresh_lattice()
        self.plotter.plot_lattice()
        self.canvas.draw()


if __name__ == '__main__':
    window = Window(None)
