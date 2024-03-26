import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

# class Window:
#     def __init__(self, plotter):
#         self.plotter = plotter
#         self.window = tk.Tk()
#         self.window.title("Lattice")
#         self.frame = tk.Frame(self.window)
#         self.frame.grid(row=0, column=0)
#         self.slider_label = ttk.Label(self.frame, text="Slider")
#         self.slider_label.grid(row=0, column=0, sticky=tk.W)
#         self.slider = ttk.Scale(self.frame, from_=-10, to=10, orient=tk.HORIZONTAL, length=200,
#                                 command=self.update_plot)
#         self.slider.grid(row=1, column=0)
#         fig = Figure(figsize=(5, 5),
#                      dpi=100)
#
#         # list of squares
#         y = [i ** 2 for i in range(101)]
#
#         # adding the subplot
#         plot1 = fig.add_subplot(111)
#
#         # plotting the graph
#         plot1.plot(y)
#
#         # creating the Tkinter canvas
#         # containing the Matplotlib figure
#         self.canvas = FigureCanvasTkAgg(fig,master=self.window)
#         self.canvas.draw()
#
#         # placing the canvas on the Tkinter window
#         # self.canvas.get_tk_widget().pack()
#
#         # creating the Matplotlib toolbar
#         # toolbar = NavigationToolbar2Tk(canvas,self.window)
#         # toolbar.update()
#
#         # placing the toolbar on the Tkinter window
#         # canvas.get_tk_widget().pack()
#
#     # self.plotter.plot_lattice()
#     #     plt = self.plotter.get_plt()
#     #     plt.show()
#     #     fig, _ = plt.subplots()
#     #
#     #     self.canvas = FigureCanvasTkAgg(fig, master=self.frame)
#     #     self.canvas.draw()
#     #     self.canvas.get_tk_widget().grid(row=0, column=1, rowspan=2)

# def update_plot(self, value):
#     self.plotter.lattice.basis.elements[0][0] = float(value)
#     self.plotter.plot_lattice()
#     fig, _ = self.plotter.get_plt().subplots()
#     canvas = FigureCanvasTkAgg(fig, master=self.frame)
#     canvas.draw()
#
# def open(self):
#     self.window.mainloop()

if __name__ == '__main__':
    def plot():
        fig = Figure(figsize=(5, 5), dpi=100)
        y = [i ** 3 for i in range(101)]
        plot1 = fig.add_subplot(111)
        plot1.plot(y)
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack()
        toolbar = NavigationToolbar2Tk(canvas, window)
        toolbar.update()
        canvas.get_tk_widget().pack()


    window = tk.Tk()
    window.title('Plotting in Tkinter')
    window.geometry("500x500")
    plot_button = tk.Button(master=window,
                            command=plot,
                            height=2,
                            width=10,
                            text="Plot")
    fig = Figure(figsize=(5, 5), dpi=100)
    y = [i ** 2 for i in range(101)]
    plot1 = fig.add_subplot(111)
    plot1.plot(y)
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, window)
    canvas.draw()
    toolbar.update()
    canvas.get_tk_widget().pack()
    plot_button.pack()
    window.mainloop()
