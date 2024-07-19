import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QVBoxLayout, QWidget, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class SliderWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Slider Window")
        self.setGeometry(100, 100, 300, 200)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)

        layout = QVBoxLayout()
        layout.addWidget(self.slider)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("icon.png"))

        tray_menu = QMenu()

        open_action = QAction("Open", self)
        open_action.triggered.connect(self.show)
        tray_menu.addAction(open_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.exit_app)
        tray_menu.addAction(exit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def exit_app(self):
        self.tray_icon.hide()
        QApplication.instance().quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SliderWindow()
    window.removeToolBar()
    window.show()
    sys.exit(app.exec_())
