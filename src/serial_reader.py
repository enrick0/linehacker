class SerialReader:
    def __init__(self, port, baudrate=9600):
        import serial

        self.serial = serial.Serial(port, baudrate)
        self.serial.flush()

    def read_signal(self):
        if self.serial.in_waiting > 0:
            line = self.serial.readline().decode("utf-8").rstrip()
            return float(line)
        return None

    def close(self):
        self.serial.close()
