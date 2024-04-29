import re
from PySide6 import QtGui, QtWidgets
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QMessageBox
import mysql.connector
from application.login.ui_forgot_password import Ui_forgot_pass

class Reset_Screen(QWidget):
    def __init__(self):
        super().__init__()

        # Create an instance of the UI class
        self.ui = Ui_forgot_pass()
        self.ui.setupUi(self)  # Set up the UI components

        # remove title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # set app logo
        login_img = QtGui.QPixmap("images/login_img.jpg")
        self.ui.label_5.setPixmap(login_img)
        self.ui.label_5.setScaledContents(True)
        self.ui.label_5.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)

        # On - loading
        self.connection = self.connect_to_mysql()

        # Connect button click event
        self.ui.btn_reset.clicked.connect(self.reset_account)
        self.ui.btn_have_acc.clicked.connect(self.have_acc)

    def connect_to_mysql(self):
        try:
            # Replace these values with your actual MySQL connection details
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="hoteldb"
            )
            if connection.is_connected():
                print("Connected to MySQL database")
                return connection

        except mysql.connector.Error as e:
            print("Error connecting to MySQL database:", e)
            self.show_message("Warning", "Error connecting to Database.")
            return None

    def show_message(self, title, message):
        QMessageBox.warning(self, title, message)

    def validation(self):
        u_name = self.ui.txt_nw_uname.text()
        u_password = self.ui.txt_nw_pass.text()
        re_password = self.ui.txt_nw_re_pass.text()

        # Check username length
        if len(u_name) > 30:
            self.show_message("Warning", "Username should not exceed 30 characters.")
            return False

        # Check if passwords match
        if u_password != re_password:
            self.show_message("Warning", "Passwords do not match.")
            return False

        # Check password length
        if len(u_password) > 8:
            self.show_message("Warning", "Password should not exceed 8 characters.")
            return False

        return True

    def reset_account(self):
        # Perform validation before proceeding
        if not self.validation():
            return

        # Extract user input
        u_name = self.ui.txt_nw_uname.text()
        u_password = self.ui.txt_nw_pass.text()

        try:
            # Create a cursor object
            cursor = self.connection.cursor()

            # Define the SQL query to update password
            query = "UPDATE login SET password = %s WHERE username = %s"

            # Execute the query
            cursor.execute(query, (u_password, u_name))

            # Commit the transaction
            self.connection.commit()

            # Display success message
            QMessageBox.information(self, "Success", "Account password updated successfully.")

            # Close the cursor
            cursor.close()

            # Redirect to login screen
            self.have_acc()

            cursor.close()

        except mysql.connector.Error as e:
            # Roll back the transaction if an error occurs
            self.connection.rollback()
            print("Error:", e)
            # Display error message
            self.show_message("Error", "Failed to update account.")


    def have_acc(self):
        from application.login.login import Login_Screen
        self.login_screen = Login_Screen()
        self.login_screen.show()
        self.close()

