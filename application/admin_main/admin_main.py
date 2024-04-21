from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from application.admin_main.ui_admin_main import Ui_MainWindow


class AdminMainScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create an instance of the UI class

        # Create an instance of the UI class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Set up the UI components

        #button
        self.ui.btn_mgt_package.clicked.connect(self.show_mgt_package)
        self.ui.btn_mgt_staff.clicked.connect(self.show_mgt_staff)
        # self.ui.btn_view_package.clicked.connect(self.show_view_package)
        # self.ui.add_package.clicked.connect(self.show_add_package)
        # self.ui.btn_add_staff.clicked.connect(self.show_add_staff)
        # self.ui.btn_view_staff.clicked.connect(self.show_view_staff)

    def update_navigation_styles(self, selected_button):
        # Reset styles for all buttons
        buttons = [self.ui.btn_dashboard, self.ui.btn_mgt_package, self.ui.btn_mgt_staff]

        for button in buttons:
            if button == selected_button:
                button.setChecked(True)
            else:
                button.setChecked(False)

    def update_navigation_styles_staff(self, selected_button):
        # Reset styles for all buttons
        buttons = [self.ui.btn_add_staff, self.ui.btn_view_staff]

        for button in buttons:
            if button == selected_button:
                button.setChecked(True)
            else:
                button.setChecked(False)

    def update_navigation_styles_package(self, selected_button):
        # Reset styles for all buttons
        buttons = [self.ui.btn_view_package, self.ui.btn_add_package]

        for button in buttons:
            if button == selected_button:
                button.setChecked(True)
            else:
                button.setChecked(False)

    #home page
    def show_mgt_package(self):
        self.ui.admin_screens.setCurrentWidget(self.ui.mgt_package)
        self.update_navigation_styles(self.ui.btn_mgt_package)
        self.ui.btn_view_package.clicked.connect(self.show_view_package)
        self.ui.btn_add_package.clicked.connect(self.show_add_package)

    def show_mgt_staff(self):
        self.ui.admin_screens.setCurrentWidget(self.ui.mgt_staff)
        self.update_navigation_styles(self.ui.btn_mgt_staff)
        self.ui.btn_add_staff.clicked.connect(self.show_add_staff)
        self.ui.btn_view_staff.clicked.connect(self.show_view_staff)

    def show_view_package(self):
        self.ui.admin_mgt_package_screens.setCurrentWidget(self.ui.view_package)
        self.update_navigation_styles_package(self.ui.btn_view_package)

    def show_add_package(self):
        self.ui.admin_mgt_package_screens.setCurrentWidget(self.ui.add_package)
        self.update_navigation_styles_package(self.ui.btn_add_package)

    def show_add_staff(self):
        self.ui.admin_mgt_package_screens_2.setCurrentWidget(self.ui.add_staff)
        self.update_navigation_styles_staff(self.ui.btn_add_staff)

    def show_view_staff(self):
        self.ui.admin_mgt_package_screens_2.setCurrentWidget(self.ui.view_staff)
        self.update_navigation_styles_staff(self.ui.btn_view_staff)
