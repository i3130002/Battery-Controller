from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
sys.path.append('.')
from tray import Tray



if __name__ == "__main__":
    app = Tray()
    app.run()
