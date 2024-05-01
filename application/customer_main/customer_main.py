import mysql
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from application.customer_main.ui_cust_main import Ui_customer_main_window


class CustomerMainScreen(QMainWindow):
    def __init__(self, c_id):
        super().__init__()

        self.c_id = c_id

        # Create an instance of the UI class
        self.ui = Ui_customer_main_window()
        self.ui.setupUi(self)  # Set up the UI components

        #button
        self.ui.btn_package.clicked.connect(self.show_packages)
        self.ui.btn_view_reser.clicked.connect(self.show_reservation)
        self.ui.btn_dashboard.clicked.connect(self.dashboard)


        #loading
        self.show_view_packages()
        self.show_view_reservation()
        self.display_name()


    def show_message(self, title, message):
        QMessageBox.warning(self, title, message)

    def connect_to_mysql(self):
        try:
            # Replace these values with your actual MySQL connection details
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="hoteldb"
            )
            if self.connection.is_connected():
                print("Connected to MySQL database")
                return self.connection

        except mysql.connector.Error as e:
            print("Error connecting to MySQL database:", e)
            self.show_message("Warning", "Error connecting to Database.")
            return None

    def display_name(self):
        cursor = self.connect_to_mysql().cursor()
        cursor.execute("SELECT username FROM login WHERE customer_id = %s", (self.c_id,))
        result = cursor.fetchone()
        print("Result:", result)  # Add this line to see the result
        if result:
            username = result[0]
            self.ui.user_name_txt.setText(username)
        else:
            self.show_message("Error", "Username not found.")

    def update_navigation_styles(self, selected_button):
        # Reset styles for all buttons
        buttons = [self.ui.btn_dashboard, self.ui.btn_package, self.ui.btn_view_reser]

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

    def update_navigation_styles_reservation(self, selected_button):
        # Reset styles for all buttons
        buttons = [self.ui.btn_view_reservations]

        for button in buttons:
            if button == selected_button:
                button.setChecked(True)
            else:
                button.setChecked(False)


    def show_packages(self):
        self.ui.cust_screens.setCurrentWidget(self.ui.mgt_package)
        self.update_navigation_styles(self.ui.btn_package)
        self.ui.btn_view_package.clicked.connect(self.show_view_packages)


    def dashboard(self):
        self.ui.cust_screens.setCurrentWidget(self.ui.dashboard)
        self.update_navigation_styles(self.ui.btn_dashboard)


        # # Clear the current contents of the frame
        # frame_layout = self.ui.frame_20.layout()
        # if frame_layout:
        #     while frame_layout.count() > 0:
        #         widget = frame_layout.takeAt(0).widget()
        #         if widget:
        #             widget.deleteLater()
        #
        # # Create layout for frame_19 if it doesn't exist
        # frame_layout = self.ui.frame_20.layout()
        # if frame_layout is None:
        #     frame_layout = QtWidgets.QVBoxLayout()
        #     self.ui.frame_20.setLayout(frame_layout)


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



    def show_reservation(self):
        self.ui.cust_screens.setCurrentWidget(self.ui.mgt_reservation_2)
        self.update_navigation_styles(self.ui.btn_view_reser)
        self.ui.btn_view_package.clicked.connect(self.show_view_reservation)


    def show_view_reservation(self):
        self.ui.package_screens.setCurrentWidget(self.ui.view_package)
        self.update_navigation_styles_reservation(self.ui.btn_view_reservations)

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
        from application.cust_package.view_reservation_section import ViewReservation
        self.view_res = ViewReservation(self.c_id)
        frame_layout.addWidget(self.view_res)
        # self.add_staff.setVisible(True)