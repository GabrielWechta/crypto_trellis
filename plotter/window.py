import tkinter as tk
from tkinter import ttk

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Window:
    def __init__(self, plotter):
        self.root = tk.Tk()
        self.root.title("Slider and Plot")
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0)
        slider_label = ttk.Label(frame, text="Slider")
        slider_label.grid(row=0, column=0, sticky=tk.W)
        self.slider = ttk.Scale(frame, from_=-10, to=10, orient=tk.HORIZONTAL, length=200, command=self.update_plot)
        self.slider.grid(row=1, column=0)
        fig, self.ax = plt.subplots()
        self.ax.set_xlabel('X values')
        self.ax.set_ylabel('Y values')
        self.canvas = FigureCanvasTkAgg(fig, master=frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=1, rowspan=2)
        # slider.bind("<ButtonRelease-1>", on_slider_move)
        self.update_plot(1)
        self.root.mainloop()

    def update_plot(self, value):
        value = float(value)
        x = np.linspace(-10, 10, 100)
        y = np.sin(value * x)
        self.ax.clear()
        self.ax.plot(x, y)
        self.canvas.draw()

    def on_slider_move(self, event):
        self.update_plot(self.slider.get())

if __name__ == '__main__':
    window = Window(None)
