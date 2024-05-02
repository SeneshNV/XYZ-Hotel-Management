from PySide6 import QtWidgets
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
        self.ui.btn_dashboard.clicked.connect(self.dashboard)
        self.ui.btn_mgt_package.clicked.connect(self.show_mgt_package)
        self.ui.btn_mgt_staff.clicked.connect(self.show_mgt_staff)
        self.ui.btn_logout.clicked.connect(self.show_logout)

        #loading
        self.show_view_staff()
        self.show_view_package()

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
        from application.package.view_packages_section import ViewPackage
        self.view_pack = ViewPackage()
        frame_layout.addWidget(self.view_pack)
        # self.view_pack.setVisible(True)

    def show_add_package(self):
        self.ui.admin_mgt_package_screens.setCurrentWidget(self.ui.add_package)
        self.update_navigation_styles_package(self.ui.btn_add_package)

        # Clear the current contents of the frame
        frame_layout = self.ui.frame_16.layout()
        if frame_layout:
            while frame_layout.count() > 0:
                widget = frame_layout.takeAt(0).widget()
                if widget:
                    widget.deleteLater()

        # Create layout for frame_19 if it doesn't exist
        frame_layout = self.ui.frame_16.layout()
        if frame_layout is None:
            frame_layout = QtWidgets.QVBoxLayout()
            self.ui.frame_16.setLayout(frame_layout)

        # Instantiate and add the AddStaff widget to the frame
        from application.package.add_package_section import AddPackage
        self.add_pack = AddPackage()
        frame_layout.addWidget(self.add_pack)
        # self.add_pack.setVisible(True)

    def show_add_staff(self):
        self.ui.admin_mgt_package_screens_2.setCurrentWidget(self.ui.add_staff)
        self.update_navigation_styles_staff(self.ui.btn_add_staff)

        # Clear the current contents of the frame
        frame_layout = self.ui.frame_19.layout()
        if frame_layout:
            while frame_layout.count() > 0:
                widget = frame_layout.takeAt(0).widget()
                if widget:
                    widget.deleteLater()

        # Create layout for frame_19 if it doesn't exist
        frame_layout = self.ui.frame_19.layout()
        if frame_layout is None:
            frame_layout = QtWidgets.QVBoxLayout()
            self.ui.frame_19.setLayout(frame_layout)

        # Instantiate and add the AddStaff widget to the frame
        from application.staff.add_staff_section import AddStaff
        self.add_staff = AddStaff()
        frame_layout.addWidget(self.add_staff)
        # self.add_staff.setVisible(True)

    def show_view_staff(self):
        self.ui.admin_mgt_package_screens_2.setCurrentWidget(self.ui.view_staff)
        self.update_navigation_styles_staff(self.ui.btn_view_staff)

        # Clear the current contents of the frame
        frame_layout = self.ui.frame_18.layout()
        if frame_layout:
            while frame_layout.count() > 0:
                widget = frame_layout.takeAt(0).widget()
                if widget:
                    widget.deleteLater()

        # Create layout for frame_19 if it doesn't exist
        frame_layout = self.ui.frame_18.layout()
        if frame_layout is None:
            frame_layout = QtWidgets.QVBoxLayout()
            self.ui.frame_18.setLayout(frame_layout)

        # Instantiate and add the AddStaff widget to the frame
        from application.staff.view_staff_section import ViewStaff
        self.view_staff = ViewStaff()
        frame_layout.addWidget(self.view_staff)
        # self.view_staff.setVisible(True)


    def dashboard(self):
        self.ui.admin_screens.setCurrentWidget(self.ui.dashboard)
        self.update_navigation_styles(self.ui.btn_dashboard)


    def show_logout(self):
        # Close the current window
        self.close()

        from application.login.login import Login_Screen
        self.login_window = Login_Screen()
        self.login_window.show()