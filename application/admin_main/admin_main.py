from PySide6.QtWidgets import QApplication, QMainWindow

class Login_Screen(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create an instance of the UI class

        self.ui.setupUi(self)  # Set up the UI components