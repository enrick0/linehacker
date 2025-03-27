# Python
import serial
import time
import random
import sys


def emulate_serial(port, baudrate=9600, interval=0.1):
    """
    Emulates an Arduino sending analog signals over a serial port.

    Args:
        port (str): The serial port to emulate (e.g., 'COM3' on Windows or '/dev/ttyS1' on Linux).
        baudrate (int): The baud rate for the serial communication.
        interval (float): Time interval (in seconds) between sending signals.
    """
    try:
        with serial.Serial(port, baudrate, timeout=1) as ser:
            print(f"Emulating serial on {port} at {baudrate} baud...")
            while True:
                # Generate a random analog signal value (e.g., 0-1023 for a 10-bit ADC)
                analog_value = random.randint(0, 1023)
                # Send the value as a string followed by a newline
                ser.write(f"{analog_value}\n".encode("utf-8"))
                print(f"Sent: {analog_value}")
                time.sleep(interval)
    except serial.SerialException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Serial emulation stopped.")


if __name__ == "__main__":
    # get first argument from command line
    port = sys.argv[1]

    emulate_serial(port=port, baudrate=9600, interval=0.1)
