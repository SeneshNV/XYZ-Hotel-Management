from PySide6 import QtGui, QtWidgets
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QMessageBox
from application.login.ui_login import Ui_login
import mysql.connector

class Login_Screen(QWidget):
    def __init__(self):
        super().__init__()

        # Create an instance of the UI class
        self.ui = Ui_login()
        self.ui.setupUi(self)  # Set up the UI components

        # remove title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # set app logo
        login_img = QtGui.QPixmap("images/login_img.jpg")
        self.ui.label_5.setPixmap(login_img)
        self.ui.label_5.setScaledContents(True)
        self.ui.label_5.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)

        #On - loading
        self.connect_to_mysql()

        # Connect button click event
        self.ui.btn_login.clicked.connect(self.login_button_clicked)

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

    def validation(self):
        u_name = self.ui.txt_u_name.text()
        u_pass = self.ui.txt_u_pass.text()

        if len(u_name) > 25:
            self.show_message("Warning", "Username should not exceed 25 characters.")
            return False

        if not u_name.strip() or not u_pass.strip():
            self.show_message("Warning", "Username and Password cannot be empty.")
            return False

        return True


    def login_button_clicked(self):
        if self.validation():
            try:
                acc_type = self.ui.cmb_u_acc_type.currentText()
                if acc_type == "Administrator Account":
                    username = self.ui.txt_u_name.text()
                    password = self.ui.txt_u_pass.text()
                    if self.validate_admin_credentials(username, password):
                        print("Credentials are valid")

                        from application.admin_main.admin_main import AdminMainScreen
                        self.admin_main_screen = AdminMainScreen()
                        self.admin_main_screen.show()
                        self.close()

                    else:
                        self.show_message("Error", "Invalid username or password for Administrator Account")
                else:
                    print("Regular user login")

            except Exception as e:
                print("Error:", e)

    def validate_admin_credentials(self, username, password):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM admin WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            cursor.close()
            return result is not None
        except mysql.connector.Error as e:
            print("Error validating credentials:", e)
            return False

