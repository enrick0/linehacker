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

        # Main layout: left column and right plot area
        self.main_frame = ctk.CTkFrame(self.master)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Left column for stats
        self.left_frame = ctk.CTkFrame(self.main_frame, width=200)
        self.left_frame.pack(side="left", fill="y", padx=10, pady=10)

        self.min_label = ctk.CTkLabel(self.left_frame, text="Min Value: N/A")
        self.min_label.pack(pady=5)

        self.max_label = ctk.CTkLabel(self.left_frame, text="Max Value: N/A")
        self.max_label.pack(pady=5)

        self.actual_label = ctk.CTkLabel(self.left_frame, text="Actual Value: N/A")
        self.actual_label.pack(pady=5)

        self.start_button = ctk.CTkButton(
            self.left_frame, text="Start", command=self.start_reading
        )
        self.start_button.pack(pady=10)

        self.stop_button = ctk.CTkButton(
            self.left_frame, text="Stop", command=self.stop_reading
        )
        self.stop_button.pack(pady=10)

        # Right frame for plot
        self.right_frame = ctk.CTkFrame(self.main_frame)
        self.right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.right_frame)
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

            # Update stats
            self.actual_label.configure(text=f"Actual Value: {value}")
            self.min_label.configure(text=f"Min Value: {min(self.data)}")
            self.max_label.configure(text=f"Max Value: {max(self.data)}")

            # Update plot
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
