import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import ctypes
import re

# Constants for Windows API
WS_EX_LAYERED = 0x80000
WS_EX_TRANSPARENT = 0x20
GWL_EXSTYLE = -20

class TransparentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #get window size from user
        
        width, height, opacity = config()
        # Set window size (can be resized or static depending on your choice)
        self.setGeometry(100, 100, width, height)

        # Get screen size
        screen_geometry = app.primaryScreen().geometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        # Calculate position to center the window
        window_x = (screen_width - self.width()) // 2
        window_y = (screen_height - self.height()) // 2

        # Move the window to the calculated position
        self.move(window_x, window_y)


        # Make the window semi-transparent
        self.setWindowOpacity(opacity)

        # Remove the window frame and keep it on top
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        # Create QLabel to hold the image and scale it to fit the window
        self.label = QLabel(self)
        pixmap = QPixmap("image.png")

        # Scale the image to fit the window size
        scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(scaled_pixmap)

        # Make the label fill the window
        self.label.resize(self.size())

        # Make the window click-through using Windows API
        hwnd = self.winId().__int__()  # Get the window handle (HWND)
        style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style | WS_EX_LAYERED | WS_EX_TRANSPARENT)


def config() -> tuple[int, int, int]:
    try:
        file = open('config.txt', 'r')
        file.close()
    except FileNotFoundError:
        file = open('config.txt', 'w')
        file.write('configurations for the program, width and length are in pixels, opacity is a number between 1 and 100\n')
        file.write('width-450\n')
        file.write('length-675\n')
        file.write('opacity-50\n')
        file.close()
        exit()

    with open('config.txt', 'r') as f:
        lines = f.readlines()
        width, height, opacity = None, None, None

        # Extract numbers from the config lines
        for line in lines:
            # Search for 'width-', 'length-', or 'opacity-' followed by the number
            if "width-" in line:
                width = int(re.search(r'width-(\d+)', line).group(1))
            elif "length-" in line:
                height = int(re.search(r'length-(\d+)', line).group(1))
            elif "opacity-" in line:
                opacity = int(re.search(r'opacity-(\d+)', line).group(1))/100

    return width, height, opacity


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create and show the transparent window with the scaled image
    window = TransparentWindow()
    window.show()

    # Run the application
    sys.exit(app.exec_())
