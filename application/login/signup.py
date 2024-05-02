import re

from PySide6 import QtGui, QtWidgets
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QMessageBox
from application.login.ui_signup import Ui_login
import mysql.connector

class Signup_Screen(QWidget):
    def __init__(self):
        super().__init__()

        # Create an instance of the UI class
        self.ui = Ui_login()
        self.ui.setupUi(self)  # Set up the UI components

        # remove title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # set app logo
        login_img = QtGui.QPixmap("images/2151038924.jpg")
        self.ui.label_5.setPixmap(login_img)
        self.ui.label_5.setScaledContents(True)
        self.ui.label_5.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)

        #On - loading
        self.connect_to_mysql()

        self.connection = self.connect_to_mysql()
        if self.connection:
            self.next_id = self.get_next_id()
            self.customer_id = "C00" + str(self.next_id)

        # Connect button click event
        self.ui.btn_signup.clicked.connect(self.signup_account)

        self.ui.btn_have_acc.clicked.connect(self.have_acc)

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
                # Optionally, you can return the connection object or store it in a class attribute for later use
                return self.connection

        except mysql.connector.Error as e:
            print("Error connecting to MySQL database:", e)
            self.show_message("Warning", "Error connecting to Database.")
            return None

    def show_message(self, title, message):
        QMessageBox.warning(self, title, message)

    def get_next_id(self):
        try:
            cursor = self.connection.cursor()
            # Execute a SQL query to get the maximum id from the staff table
            query = "SELECT MAX(id) FROM login"
            cursor.execute(query)
            result = cursor.fetchone()  # Fetch the result of the query

            if result and result[0] is not None:
                # If there are existing records, increment the maximum id to get the next available id
                next_id = result[0] + 1
            else:
                # If there are no existing records, start with id = 1
                next_id = 1

            return next_id

        except mysql.connector.Error as e:
            print("Error:", e)
            # Handle the error accordingly, such as displaying an error message or logging the error
            return None

    def validation(self):
        u_name = self.ui.txt_nw_uname.text()
        u_email = self.ui.txt_nw_email.text()
        u_password = self.ui.txt_nw_pass.text()
        re_password = self.ui.txt_nw_re_pass.text()

        # Check username length
        if len(u_name) > 30:
            self.show_message("Warning", "Username should not exceed 30 characters.")
            return False

        # Check email validity using a regular expression
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", u_email):
            self.show_message("Warning", "Please enter a valid email address.")
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

    def signup_account(self):
        # Perform validation before proceeding
        if not self.validation():
            return

        # Extract user input
        u_name = self.ui.txt_nw_uname.text()
        u_email = self.ui.txt_nw_email.text()
        u_password = self.ui.txt_nw_pass.text()

        try:
            # Create a cursor object
            cursor = self.connection.cursor()

            # Check if the username already exists
            cursor.execute("SELECT username FROM login WHERE username = %s", (u_name,))
            existing_username = cursor.fetchone()
            if existing_username:
                # Display error message if the username already exists
                self.show_message("Error", "Username already exists. Please choose a different username.")
                return

            # Define the SQL query to insert data into the login table
            query = "INSERT INTO login (customer_id, username, password, email) VALUES (%s, %s, %s, %s)"

            # Execute the query
            cursor.execute(query, (self.customer_id, u_name, u_password, u_email))

            # Commit the transaction
            self.connection.commit()

            # Display success message
            QMessageBox.information(self, "Success", "Account created successfully.")

            self.have_acc()

        except mysql.connector.Error as e:
            # Roll back the transaction if an error occurs
            self.connection.rollback()
            print("Error:", e)
            # Display error message
            self.show_message("Error", "Failed to create account.")

        finally:
            # Close the cursor
            cursor.close()

    def have_acc(self):
        from application.login.login import Login_Screen
        self.Login_Screen = Login_Screen()
        self.Login_Screen.show()
        self.close()
