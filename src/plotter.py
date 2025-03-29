class Plotter:
    def __init__(self):
        import matplotlib.pyplot as plt
        from matplotlib.animation import FuncAnimation

        self.fig, self.ax = plt.subplots()
        self.x_data = []
        self.y_data = []
        (self.line,) = self.ax.plot([], [], "r-")
        self.ax.set_xlim(0, 100)  # Adjust as necessary
        self.ax.set_ylim(0, 1023)  # Assuming 10-bit ADC from Arduino
        self.ax.set_ylabel("KN")  # Add unit to y-axis label

    def init_plot(self):
        self.line.set_data([], [])
        return (self.line,)

    def update_plot(self, new_data):
        self.x_data.append(len(self.x_data))
        self.y_data.append(new_data)

        self.line.set_data(self.x_data, self.y_data)
        return (self.line,)

    def show(self):
        ani = FuncAnimation(
            self.fig, self.update_plot, init_func=self.init_plot, blit=True
        )
        plt.show()
