from PySide6 import QtGui, QtWidgets, QtCore
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget
from application.splash.ui_splash_screen_ui import Ui_splash_screen
from application.login.login import Login_Screen


#Global Variables
COUNTER = 0

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create an instance of the UI class
        self.ui = Ui_splash_screen()
        self.ui.setupUi(self)  # Set up the UI components

        # remove title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # set app logo
        splash_img = QtGui.QPixmap("images/splash_img.jpg")
        self.ui.label_5.setPixmap(splash_img)
        self.ui.label_5.setScaledContents(True)
        self.ui.label_5.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)

        # QTimer
        self.progress_timer = QtCore.QTimer()
        self.progress_timer.timeout.connect(self.progress)

        # timer in milisecond
        self.progress_timer.start(35)

        # progress bar function

    def progress(self):
        global COUNTER

        # set value to progress bar
        self.ui.progressBar.setValue(COUNTER)
        self.ui.label_4.setText(f"{int(COUNTER)}% Loading...")

        # close splash screen
        if COUNTER > 100:
            # stop timer
            self.progress_timer.stop()

            # show logn in screen
            self.login = Login_Screen()
            self.login.show()

            # close splash screen
            self.close()
        # increase counter
        COUNTER += 5