"""
╔═══════════════════════════════════════════════════════════╗
║                  DEOX COLORBOT SYSTEM                     ║
║          Advanced Arduino-Based Aim Assistance            ║
║                                                           ║
║  Developer: Deox                                          ║
║  Version: 2.0                                             ║
║  License: Educational Use Only                            ║
╚═══════════════════════════════════════════════════════════╝
"""

import pyautogui
import os
import sys
from datetime import datetime
from colorbot import Colorbot
from settings import Settings

class DEOXMain:
    """
    The DEOXMain class initializes the DEOX application, sets up the necessary parameters,
    and manages the colorbot system with enhanced error handling and user feedback.
    """

    # ANSI color codes for enhanced terminal output
    class Colors:
        HEADER = '\033[95m'
        BLUE = '\033[94m'
        CYAN = '\033[96m'
        GREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    def __init__(self):
        """
        Initializes the DEOXMain class by setting up screen parameters and the Colorbot instance.

        Attributes:
            settings (Settings): The settings instance for reading configuration files.
            monitor (tuple): The screen resolution.
            center_x (int): The center X-coordinate of the screen.
            center_y (int): The center Y-coordinate of the screen.
            x_fov (int): The width of the capture area.
            y_fov (int): The height of the capture area.
            colorbot (Colorbot): The Colorbot instance for screen capturing and color detection.
        """
        try:
            self.settings = Settings()
            
            # Get screen resolution
            self.monitor = pyautogui.size()
            self.center_x, self.center_y = self.monitor.width // 2, self.monitor.height // 2
            
            # Load FOV settings
            self.x_fov = self.settings.get_int('Aimbot', 'xFov')
            self.y_fov = self.settings.get_int('Aimbot', 'yFov')

            # Initialize colorbot with calculated parameters
            self.colorbot = Colorbot(
                self.center_x - self.x_fov // 2, 
                self.center_y - self.y_fov // 2, 
                self.x_fov, 
                self.y_fov
            )
            
        except Exception as e:
            self._print_error(f"Initialization failed: {str(e)}")
            input("\nPress Enter to exit...")
            sys.exit(1)

    def _print_header(self):
        """
        Prints the DEOX branded header with system information.
        """
        header = f"""
{self.Colors.CYAN}╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║  ████████╗ ██████╗   ██████╗  ██╗  ██╗                    ║
║  ██╔═══██║ ██╔═════ ██╔═══██╗ ╚██╗██╔╝                    ║
║  ██║   ██║ █████╗   ██║   ██║  ╚███╔╝                     ║
║  ██║   ██║ ██╔══╝   ██║   ██║  ██╔██╗                     ║
║  ████████║ ███████╗ ╚██████╔╝ ██╔╝ ██╗                    ║
║  ╚═══════╝ ╚══════╝  ╚═╝  ╚═╝                             ║
║                                                           ║
║            ADVANCED COLORBOT SYSTEM v2.0                  ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝{self.Colors.ENDC}

{self.Colors.BOLD}System Information:{self.Colors.ENDC}
{self.Colors.GREEN}├─{self.Colors.ENDC} Developer    : Deox
{self.Colors.GREEN}├─{self.Colors.ENDC} Version      : 2.0.0
{self.Colors.GREEN}├─{self.Colors.ENDC} Resolution   : {self.monitor.width}x{self.monitor.height}
{self.Colors.GREEN}├─{self.Colors.ENDC} FOV          : {self.x_fov}x{self.y_fov}
{self.Colors.GREEN}├─{self.Colors.ENDC} Started      : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{self.Colors.GREEN}└─{self.Colors.ENDC} Status       : {self.Colors.GREEN}OPERATIONAL{self.Colors.ENDC}

{self.Colors.WARNING}⚠️  Educational Use Only - Use at Your Own Risk{self.Colors.ENDC}
"""
        print(header)

    def _print_config(self):
        """
        Prints the current configuration settings.
        """
        config = f"""
{self.Colors.BOLD}Configuration:{self.Colors.ENDC}
{self.Colors.CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{self.Colors.ENDC}

{self.Colors.BLUE}[Aimbot]{self.Colors.ENDC}
  • Status         : {self.Colors.GREEN + 'ENABLED' if self.settings.get_boolean('Aimbot', 'Enabled') else self.Colors.FAIL + 'DISABLED'}{self.Colors.ENDC}
  • Activation Key : Right Mouse Button
  • Speed (X/Y)    : {self.settings.get_float('Aimbot', 'xSpeed')}/{self.settings.get_float('Aimbot', 'ySpeed')}
  • Target Offset  : {self.settings.get_float('Aimbot', 'targetOffset')} pixels

{self.Colors.BLUE}[Triggerbot]{self.Colors.ENDC}
  • Status         : {self.Colors.GREEN + 'ENABLED' if self.settings.get_boolean('Triggerbot', 'Enabled') else self.Colors.FAIL + 'DISABLED'}{self.Colors.ENDC}
  • Activation Key : Left Alt
  • Delay Range    : {self.settings.get_int('Triggerbot', 'minDelay')}-{self.settings.get_int('Triggerbot', 'maxDelay')}ms
  • Trigger Zone   : {self.settings.get_int('Triggerbot', 'xRange')}x{self.settings.get_int('Triggerbot', 'yRange')} pixels

{self.Colors.BLUE}[Detection]{self.Colors.ENDC}
  • Target Color   : {self.Colors.HEADER}Purple (HSV Optimized){self.Colors.ENDC}
  • Capture Method : MSS (High Performance)

{self.Colors.CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{self.Colors.ENDC}
{self.Colors.GREEN}✓ System Ready - Hold activation keys to engage{self.Colors.ENDC}
"""
        print(config)

    def _print_error(self, message):
        """
        Prints an error message with formatting.
        
        Args:
            message (str): The error message to display.
        """
        print(f"\n{self.Colors.FAIL}[ERROR]{self.Colors.ENDC} {message}")

    def run(self):
        """
        Executes the main application loop with enhanced UI and error handling.
        """
        try:
            # Clear screen and set window title
            os.system('cls')
            os.system('title DEOX Colorbot System v2.0 - Advanced Aim Assistance')
            
            # Display branded interface
            self._print_header()
            self._print_config()
            
            # Start colorbot listener
            print(f"\n{self.Colors.CYAN}[INFO]{self.Colors.ENDC} Starting colorbot listeners...")
            self.colorbot.listen()
            
            # Keep main thread alive
            print(f"{self.Colors.GREEN}[SUCCESS]{self.Colors.ENDC} All systems operational\n")
            
            # Infinite loop to keep the program running
            while True:
                pass
                
        except KeyboardInterrupt:
            print(f"\n\n{self.Colors.WARNING}[SHUTDOWN]{self.Colors.ENDC} DEOX system terminated by user")
            sys.exit(0)
        except Exception as e:
            self._print_error(f"Runtime error: {str(e)}")
            input("\nPress Enter to exit...")
            sys.exit(1)

if __name__ == '__main__':
    DEOXMain().run()