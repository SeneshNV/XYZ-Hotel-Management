import os
import shutil
import re

from PySide6.QtCore import QSize
from PySide6.QtGui import Qt, QPixmap, QPainter, QPainterPath
from PySide6.QtWidgets import QWidget, QMessageBox, QVBoxLayout, QLabel, QPushButton, \
    QListWidget, QListWidgetItem, QHBoxLayout, QSpacerItem, QSizePolicy, QLineEdit, QTextEdit, QComboBox, QFileDialog
from application.package.ui_add_package import Ui_add_package_form
import mysql.connector

class AddPackage(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_add_package_form()
        self.ui.setupUi(self)  # Set up the UI components

        # Remove title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        print("Open add package add section")
        self.connection = self.connect_to_mysql()
        if self.connection:
            self.next_id = self.get_next_id()
            self.package_id = "P00" + str(self.next_id)

        #button
        self.ui.btn_browser_img_2.clicked.connect(self.upload_package_image)
        self.ui.btn_save_package_2.clicked.connect(self.insert_package)

        # Initialize image file names
        self.pkp_image_name = ""


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

    def get_next_id(self):
        try:
            cursor = self.connection.cursor()
            # Execute a SQL query to get the maximum id from the staff table
            query = "SELECT MAX(id) FROM packages"
            cursor.execute(query)
            result = cursor.fetchone()  # Fetch the result of the query

            if result and result[0] is not None:
                # If there are existing records, increment the maximum id to get the next available id
                next_id = result[0] + 1
            else:
                # If there are no existing records, start with id = 1
                next_id = 1

            # Set the text of the QLineEdit widget named 'upload_s_id_2'
            self.ui.txt_p_id.setText("P00" + str(next_id))

            return next_id

        except mysql.connector.Error as e:
            print("Error:", e)
            # Handle the error accordingly, such as displaying an error message or logging the error
            return None


    def upload_package_image(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Upload Image", "", "Images (*.png *.jpg *.bmp);;All Files (*)",
                                                  options=options)
        if filename:
            # Get the file extension
            _, extension = os.path.splitext(filename)

            # Construct the path to the image repository folder relative to the application directory
            app_folder = os.path.dirname(__file__)
            image_repo_path = os.path.join(app_folder, "image_repo")

            # Save the image to the image repository folder with the name = next_id and the correct extension
            self.pkp_image_name = f"{self.package_id}{extension}"
            image_dest_path = os.path.join(image_repo_path, self.pkp_image_name)
            os.makedirs(image_repo_path, exist_ok=True)  # Create folder if it doesn't exist
            shutil.copy(filename, image_dest_path)  # Move image to destination

            # Display success message or perform other actions
            print("Package image uploaded successfully!")
            # self.show_message("Successful", "Profile picture uploaded successfully!")

            # Load the image into a QPixmap object
            pixmap = QPixmap(image_dest_path)

            # Resize the pixmap to 100x100
            pixmap = pixmap.scaled(240, 160, Qt.KeepAspectRatio)

            # Set the QPixmap object as the pixmap for the label
            self.ui.lbl_display_img_2.setPixmap(pixmap)  # Display the uploaded image

    def insert_package(self):
        try:
            cursor = self.connection.cursor()

            # Validate input
            if not self.validate_input():
                return

            # Get values from UI components
            p_id = self.package_id
            p_name = self.ui.txt_p_title.text()
            cost_per_person = 1
            description = self.ui.txt_p_description.toPlainText()

            # Get complementary checkboxes that are checked
            complementary_checkboxes = [
                "FREE WIFI" if self.ui.chk_com_wifi.isChecked() else "",
                "24HR SECURITY " if self.ui.chk_com_security.isChecked() else "",
                "BUTLER SERVICE" if self.ui.chk_com_butler_service.isChecked() else "",
                "CAR PARKING" if self.ui.chk_com_car.isChecked() else "",
                "INFINITY POOL" if self.ui.chk_com_pool.isChecked() else "",
                "24HR SERVICE" if self.ui.chk_com_24hr_service.isChecked() else "",
            ]

            # Filter out empty strings (unchecked checkboxes)
            complementary = ', '.join(filter(None, complementary_checkboxes))

            category = ""
            p_image = self.pkp_image_name

            # Define the INSERT query with placeholders
            insert_query = """
            INSERT INTO packages (p_id, p_name, cost_per_person, description, complementary, category, p_image) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            # Execute the query with the values
            cursor.execute(insert_query, (
                p_id, p_name, cost_per_person, description, complementary, category, p_image))

            # Commit the transaction
            self.connection.commit()

            print("Package inserted successfully!")
            QMessageBox.information(self, "Success", "Package inserted successfully!")
            # Reset the form
            self.reset_form()

            cursor.close()

        except mysql.connector.Error as e:
            print("Error:", e)
            # Handle the error accordingly, such as displaying an error message or logging the error


    def validate_input(self):
        # Get values from UI components
        p_name = self.ui.txt_p_title.text()
        description = self.ui.txt_p_description.toPlainText()
        p_image = self.pkp_image_name


        # Validate required fields
        if not p_name.strip():
            self.show_message("Validation Error", "Please enter a name.")
            return False
        elif len(p_name) > 30:
            self.show_message("Validation Error", "Name must be at most 30 characters long.")
            return False
        elif p_name.isdigit():  # Check if name contains only digits
            self.show_message("Validation Error", "Name cannot contain only numbers.")
            return False
        elif not description.strip():
            self.show_message("Validation Error", "Please enter a Description.")
            return False
        elif len(description) > 300:
            self.show_message("Validation Error", "Description must be at most 300 characters long.")
            return False
        elif not p_image:
            self.show_message("Validation Error", "Please upload a profile picture.")
            return False
        elif not self.ui.chk_price.isChecked():
            self.show_message("Validation Error", "Please check Standard Price Method.")
            return False
        
        return True

    def reset_form(self):
        # Reset input fields
        self.ui.txt_p_title.clear()
        self.ui.txt_p_description.clear()
        self.ui.lbl_display_img_2.clear()

        # Update next ID
        self.next_id = self.get_next_id()
        self.package_id = "P00" + str(self.next_id)
        self.ui.txt_p_id.setText("P00" + str(self.next_id))

        self.pkp_image_name = ""