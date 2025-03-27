import tkinter as tk
from tkinter import messagebox
import serial
import time
from gui import App
from serial_reader import SerialReader
from customtkinter import *


def main():
    # Initialize the Tkinter root window
    root = CTk()
    root.title("Ardyno Analog Signal Reader")

    # Set up the serial reader
    try:
        serial_reader = SerialReader(
            port="/dev/pts/4", baudrate=9600
        )  # Adjust port as necessary
    except Exception as e:
        messagebox.showerror("Error", f"Could not open serial port: {e}")
        return

    # Create the GUI application
    app = App(root, serial_reader)

    # Start the main event loop
    root.mainloop()

    # Close the serial connection on exit
    serial_reader.close()


if __name__ == "__main__":
    main()
