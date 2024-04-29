from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from application.customer_main.ui_cust_main import Ui_customer_main_window


class CustomerMainScreen(QMainWindow):
    def __init__(self, c_id):
        super().__init__()

        self.c_id = c_id

        # Create an instance of the UI class
        self.ui = Ui_customer_main_window()
        self.ui.setupUi(self)  # Set up the UI components

        #button
        self.ui.btn_package.clicked.connect(self.show_packages())
        # self.ui.btn_mgt_staff.clicked.connect(self.show_mgt_staff)

        #loading
        self.show_view_packages()
        # self.show_view_package()


    def update_navigation_styles(self, selected_button):
        # Reset styles for all buttons
        buttons = [self.ui.btn_dashboard, self.ui.btn_package]

        for button in buttons:
            if button == selected_button:
                button.setChecked(True)
            else:
                button.setChecked(False)

    def update_navigation_styles_staff(self, selected_button):
        # Reset styles for all buttons
        buttons = [self.ui.btn_view_package]

        for button in buttons:
            if button == selected_button:
                button.setChecked(True)
            else:
                button.setChecked(False)


    def show_packages(self):
        self.ui.cust_screens.setCurrentWidget(self.ui.mgt_package)
        self.update_navigation_styles(self.ui.btn_package)
        self.ui.btn_view_package.clicked.connect(self.show_view_packages)


    def show_view_packages(self):
        self.ui.package_screens.setCurrentWidget(self.ui.view_package)
        self.update_navigation_styles_staff(self.ui.btn_view_package)

        # Clear the current contents of the frame
        frame_layout = self.ui.frame_17.layout()
        if frame_layout:
            while frame_layout.count() > 0:
                widget = frame_layout.takeAt(0).widget()
                if widget:
                    widget.deleteLater()

        # Create layout for frame_19 if it doesn't exist
        frame_layout = self.ui.frame_17.layout()
        if frame_layout is None:
            frame_layout = QtWidgets.QVBoxLayout()
            self.ui.frame_17.setLayout(frame_layout)

        # Instantiate and add the AddStaff widget to the frame
        from application.cust_package.cust_view_package_section import ViewPackage
        self.view_pack = ViewPackage(self.c_id)
        frame_layout.addWidget(self.view_pack)
        # self.add_staff.setVisible(True)