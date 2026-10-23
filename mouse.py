"""
╔═══════════════════════════════════════════════════════════╗
║          DEOX MOUSE - Arduino Control Interface           ║
║       Hardware-Level Mouse Control via Serial Port        ║
╚═══════════════════════════════════════════════════════════╝
"""

import time
import threading
import serial
import serial.tools.list_ports
from settings import Settings

class Mouse:
    """
    DEOX Mouse - Arduino Serial Communication Controller
    
    This class provides a robust interface for communicating with Arduino Leonardo
    to control mouse movements at the hardware level, bypassing software-based detection.
    
    Features:
        - Automatic COM port detection based on settings.ini configuration
        - Thread-safe serial communication with mutex locking
        - Sub-pixel movement tracking with remainder accumulation
        - High-speed 115200 baud rate for minimal latency
        - Graceful error handling for connection issues
        - Supports both move and click commands
    
    Communication Protocol:
        - Move: "M<x>,<y>\n" (e.g., "M10,-5\n")
        - Click: "C\n"
    
    Attributes:
        settings (Settings): Configuration manager instance
        serial_port (serial.Serial): Arduino serial connection
        lock (threading.Lock): Thread synchronization for serial writes
        remainder_x (float): Accumulated x-axis fractional movement
        remainder_y (float): Accumulated y-axis fractional movement
    """
    
    def __init__(self):
        """
        Initializes the Mouse class by setting up the serial port connection to the Arduino
        and initializing the remainder attributes.
        """
        self.settings = Settings()
        self.lock = threading.Lock()
        self.serial_port = serial.Serial()
        self.serial_port.baudrate = 115200
        self.serial_port.timeout = 0
        self.serial_port.port = self.find_serial_port()
        self.remainder_x = 0.0
        self.remainder_y = 0.0
        try:
            self.serial_port.open()
            print(f"[DEOX] ✓ Connected to Arduino on {self.serial_port.port}")
        except serial.SerialException as e:
            print(f"\n[DEOX ERROR] Failed to connect to Arduino!")
            print(f"Reason: {str(e)}")
            print("\nPossible causes:")
            print("  • DEOX is already running")
            print("  • Arduino is being used by another application")
            print("  • COM port is incorrect in settings.ini")
            print("  • Arduino is not connected")
            print("\nExiting in 10 seconds...")
            time.sleep(10)
            exit()

    def find_serial_port(self):
        """
        Finds and returns the serial port connected to the Arduino based on the configuration settings.

        Returns:
            str: The device name of the connected serial port.

        Raises:
            SystemExit: If the specified Arduino COM port cannot be found.
        """
        com_port = self.settings.get('Settings', 'COM-Port')
        port = next((port for port in serial.tools.list_ports.comports() if com_port in port.description), None)
        if port is not None:
            return port.device
        else:
            print(f"\n[DEOX ERROR] Arduino not detected on {com_port}!")
            print("\nAvailable COM ports:")
            available_ports = serial.tools.list_ports.comports()
            if available_ports:
                for p in available_ports:
                    print(f"  • {p.device}: {p.description}")
            else:
                print("  • No COM ports detected")
            print(f"\nPlease verify:")
            print("  1. Arduino Leonardo is connected via USB")
            print("  2. COM-Port in settings.ini matches your Arduino")
            print("  3. Arduino drivers are installed")
            print("\nExiting in 10 seconds...")
            time.sleep(10)
            exit()

    def move(self, x, y):
        """
        Sends a mouse movement command to the Arduino, handling fractional movements by storing remainders.

        Args:
            x (float): The movement along the x-axis.
            y (float): The movement along the y-axis.
        """
        # Add the remainder from the previous calculation
        x += self.remainder_x
        y += self.remainder_y

        # Round x and y, and calculate the new remainder
        move_x = int(x)
        move_y = int(y)
        self.remainder_x = x - move_x
        self.remainder_y = y - move_y

        if move_x != 0 or move_y != 0:
            with self.lock:
                self.serial_port.write(f'M{move_x},{move_y}\n'.encode())

    def click(self):
        """
        Sends a mouse click command to the Arduino.
        """
        with self.lock: 
            self.serial_port.write('C\n'.encode())