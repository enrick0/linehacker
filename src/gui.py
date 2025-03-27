from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import threading
import time
from serial_reader import SerialReader
import customtkinter as ctk


class App:
    def __init__(self, master, serial=None):
        self.master = master
        self.master.title("Arduino Analog Signal Reader")
        self.master.geometry("800x600")
        self.frame = ctk.CTkFrame(self.master)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.start_button = ctk.CTkButton(
            self.frame, text="Start", command=self.start_reading
        )
        self.start_button.pack(pady=10)

        self.stop_button = ctk.CTkButton(
            self.frame, text="Stop", command=self.stop_reading
        )
        self.stop_button.pack(pady=10)

        self.label = ctk.CTkLabel(self.frame, text="Analog Signal Value: ")
        self.label.pack(pady=10)

        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame)
        self.canvas.get_tk_widget().pack(pady=10)

        self.serial_reader = serial
        self.data = []
        self.running = False

    def start_reading(self):
        self.running = True
        self.update_plot()

    def stop_reading(self):
        self.running = False

    def update_plot(self):
        if self.running:
            value = self.serial_reader.read_signal()
            self.data.append(value)
            self.label.configure(text=f"Analog Signal Value: {value}")

            self.ax.clear()
            self.ax.plot(self.data, label="Analog Signal")
            self.ax.legend()
            self.canvas.draw()

            self.master.after(100, self.update_plot)


def main():
    ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

    root = ctk.CTk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
