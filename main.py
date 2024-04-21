import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from application.splash.splash import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
