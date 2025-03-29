import csv
import time
import datetime


class BufferSaver:
    def __init__(self):
        self.buffer = []  # List to store (time, value) tuples

    def add_element(self, value):
        """Add a new element with the current time in milliseconds and given value."""
        current_time = int(time.time() * 1000)  # Current time in milliseconds
        self.buffer.append((current_time, value))

    def save_to_csv(self, file_path=None):
        """Save the buffer to a CSV file."""
        if file_path is None:
            file_path = f"output_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
        with open(file_path, mode="w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Time (ms)", "Value"])  # Write header
            writer.writerows(self.buffer)  # Write buffer content
