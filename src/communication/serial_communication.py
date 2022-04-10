import serial
from .communication import Communication

class SerialCommunication(Communication):

    def __init__(self, port, baud_rate):
        self.ser = serial.Serial(port, baud_rate)

    def readline(self) -> bytes:
        return self.ser.readline()
    
    def write(self, data: bytes):
        self.ser.write(data)