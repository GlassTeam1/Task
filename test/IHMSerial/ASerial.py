#! /Users/ewen/anaconda3/bin/python3.5
# coding: utf8

"""Serial class for Controller."""


import serial.tools.list_ports
from threading import Thread


class ArduinoSerial:
    """Serial class to communicate with arduino."""

    def __init__(self):
        """Init."""
        self.ser = None
        self.buffer = []

    @staticmethod
    def availableDevices(self):
        """Return available serial devices."""
        return serial.tools.list_ports.comports()

    @staticmethod
    def close(self):
        """Close serial connection."""
        serial.Serial().close()

    def connect(self, device, baudrate=9600):
        """Connect to serial device."""
        Thread(target=self._reader).start()
        self.ser = serial.Serial(device, baudrate)

    def write(self, string):
        """Send a string to Arduino Board."""
        if self.isOpen:
            self.ser.write(string.encode())
        else:
            print("ERROR : NOTHING WAS SENT")

    def _reader(self):
        while True:
            try:
                tmp = self.ser.readline().decode("utf-8").strip('\r\n')
                if tmp != "" or tmp != '\n':
                    self.stack.append(tmp)
            except:
                pass

    @property
    def isOpen(self):
        """Test if serial connection is open."""
        return serial.Serial().is_open
