from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import utils
import os

class Tray:
    def __init__(self):
        # Create a Qt application
        self.app = QApplication(sys.argv)
        # Get current path
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        icon = QIcon(f"{self.current_path}/assets/battery_not_charging.png")
        menu = QMenu()
        action_to_100 = menu.addAction("To 100")
        action_to_80 = menu.addAction("To 80")
        action_to_60 = menu.addAction("To 60")
        menu.addSection("Ex2")
        self.target = menu.addMenu(f"Target:{utils.get_charging_percentage()}")
        menu.addSection("Ex")
        exitAction = menu.addAction("exit")
        action_to_100.triggered.connect(self.set_to_100)
        action_to_80.triggered.connect(self.set_to_80)
        action_to_60.triggered.connect(self.set_to_60)
        exitAction.triggered.connect(sys.exit)

        self.tray = QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.setContextMenu(menu)
        self.tray.show()
        self.tray.setToolTip("Battery Charge Control")
        self.tray.showMessage("Battery Charge Control", "I'm here ;)")

    def run(self):
        # Enter Qt application main loop
        self.app.exec_()
        sys.exit()
    
    def set_charging(self, percentage:int):
        utils.set_charging_percentage(percentage)
        self.charge_target = utils.get_charging_percentage()
        self.target.setTitle("Target:" + str(self.charge_target))
        self.tray.showMessage(f"Set to {self.charge_target}%", f"Battery Charge Control set to {self.charge_target}%")


    def set_to_100(self):
        self.set_charging(100)
    
    def set_to_80(self):
        self.set_charging(80)
    
    def set_to_60(self):
        self.set_charging(60)


if __name__ == "__main__":
    app = Tray()
    app.run()
