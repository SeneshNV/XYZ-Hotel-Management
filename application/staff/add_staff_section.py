import os
import shutil
import re

from PySide6.QtGui import Qt, QPixmap
from PySide6.QtWidgets import QWidget, QMessageBox, QFileDialog
from application.staff.ui_add_staff import Ui_add_staff_form
import mysql.connector

class AddStaff(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_add_staff_form()
        self.ui.setupUi(self)  # Set up the UI components

        # remove title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        print("Open add staff section")
        self.connection = self.connect_to_mysql()
        if self.connection:
            self.next_id = self.get_next_id()
            self.staff_id = "S00" + str(self.next_id)

            # Initialize image file names
            self.spp_image_name = ""  # Profile picture
            self.sgc_image_name = ""  # Grama Niladhari Certificate
            self.spc_image_name = ""  # Police Report

        # Connect button signals
        self.ui.save_insert_data.clicked.connect(self.insert_staff)
        self.ui.upload_staff_pp.clicked.connect(self.upload_staff_image)
        self.ui.s_upload_g_certificate.clicked.connect(self.upload_staff_G_Certificate)
        self.ui.s_upload_p_certificate.clicked.connect(self.upload_staff_P_Certificate)

        self.ui.upload_s_department.currentTextChanged.connect(self.update_salary)

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
                # Optionally, you can return the connection object or store it in a class attribute for later use
                return self.connection

        except mysql.connector.Error as e:
            print("Error connecting to MySQL database:", e)
            self.show_message("Warning", "Error connecting to Database.")
            return None

    def get_next_id(self):
        try:
            cursor = self.connection.cursor()
            # Execute a SQL query to get the maximum id from the staff table
            query = "SELECT MAX(id) FROM staff"
            cursor.execute(query)
            result = cursor.fetchone()  # Fetch the result of the query

            if result and result[0] is not None:
                # If there are existing records, increment the maximum id to get the next available id
                next_id = result[0] + 1
            else:
                # If there are no existing records, start with id = 1
                next_id = 1

            # Set the text of the QLineEdit widget named 'upload_s_id_2'
            self.ui.upload_s_id_2.setText("S00" + str(next_id))

            return next_id

        except mysql.connector.Error as e:
            print("Error:", e)
            # Handle the error accordingly, such as displaying an error message or logging the error
            return None

    from PySide6.QtGui import QPixmap

    # your other imports and class definition...

    def upload_staff_image(self):
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
            self.spp_image_name = f"{self.staff_id}{extension}"
            image_dest_path = os.path.join(image_repo_path, self.spp_image_name)
            os.makedirs(image_repo_path, exist_ok=True)  # Create folder if it doesn't exist
            shutil.copy(filename, image_dest_path)  # Move image to destination

            # Display success message or perform other actions
            print("Profile picture uploaded successfully!")
            # self.show_message("Successful", "Profile picture uploaded successfully!")

            # Load the image into a QPixmap object
            pixmap = QPixmap(image_dest_path)

            # Resize the pixmap to 100x100
            pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio)

            # Set the QPixmap object as the pixmap for the label
            self.ui.upload_staff_member_pp_2.setPixmap(pixmap)  # Display the uploaded image

    def upload_staff_G_Certificate(self):
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
            self.sgc_image_name = f"GC_{self.staff_id}{extension}"
            image_dest_path = os.path.join(image_repo_path, self.sgc_image_name)
            os.makedirs(image_repo_path, exist_ok=True)  # Create folder if it doesn't exist
            shutil.copy(filename, image_dest_path)  # Move image to destination

            # Display success message or perform other actions
            print("Grama Niladhari Certificate uploaded successfully!")
            # self.show_message("Successful", "Grama Niladhari Certificate uploaded successfully!")

            # Load the image into a QPixmap object
            pixmap = QPixmap(image_dest_path)

            # Resize the pixmap to 100x100
            pixmap = pixmap.scaled(240, 140, Qt.KeepAspectRatio)

            # Set the QPixmap object as the pixmap for the label
            self.ui.view_s_upload_g_certificate.setPixmap(pixmap)  # Display the uploaded image

    def upload_staff_P_Certificate(self):
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
            self.spc_image_name = f"PC_{self.staff_id}{extension}"
            image_dest_path = os.path.join(image_repo_path, self.spc_image_name)
            os.makedirs(image_repo_path, exist_ok=True)  # Create folder if it doesn't exist
            shutil.copy(filename, image_dest_path)  # Move image to destination

            # Display success message or perform other actions
            print("Police Report uploaded successfully!")
            # self.show_message("Successful", "Police Report uploaded successfully!")

            # Load the image into a QPixmap object
            pixmap = QPixmap(image_dest_path)

            # Resize the pixmap to 100x100
            pixmap = pixmap.scaled(240, 140, Qt.KeepAspectRatio)

            # Set the QPixmap object as the pixmap for the label
            self.ui.view_s_upload_p_certificate.setPixmap(pixmap)  # Display the uploaded image

    def update_salary(self):
        # Get the current department selected by the user
        department = self.ui.upload_s_department.currentText()

        # Calculate the salary based on the selected department
        salary = self.calculate_salary(department)

        # Update the salary field in the UI
        self.ui.upload_s_salary_2.setText(str(salary))

    def calculate_salary(self, department):
        # Dictionary to map department to salary
        department_salary = {
            "Maintenance": "Rs.45000",
            "Kitchen": "Rs.50000",
            "Housekeeping": "Rs.30000",
            "Banquets": "Rs.60000"
        }

        # Get the salary based on the selected department
        return department_salary.get(department, 0)

    def insert_staff(self):
        try:
            cursor = self.connection.cursor()

            # Validate input
            if not self.validate_input():
                return

            # Define the INSERT query with placeholders
            insert_query = """
            INSERT INTO staff (staff_id, s_name, s_photo, s_gender, s_department, s_address, s_contact_no, s_email, s_salary, s_g_certificate, s_p_certificate) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            # Get values from UI components
            staff_id = self.staff_id
            s_name = self.ui.upload_s_name_2.text()
            s_photo = self.spp_image_name
            s_gender = self.ui.upload_s_gender.currentText()
            s_department = self.ui.upload_s_department.currentText()
            s_address = self.ui.upload_s_address_2.toPlainText()
            s_contact_no = self.ui.upload_s_tel_2.text()
            s_email = self.ui.upload_s_email_2.text()
            s_salary = self.ui.upload_s_salary_2.text()
            s_g_certificate = self.sgc_image_name
            s_p_certificate = self.spc_image_name

            # Execute the query with the values
            cursor.execute(insert_query, (
            staff_id, s_name, s_photo, s_gender, s_department, s_address, s_contact_no, s_email, s_salary, s_g_certificate,
            s_p_certificate))

            # Commit the transaction
            self.connection.commit()

            print("Staff inserted successfully!")
            QMessageBox.information(self, "Success", "Staff inserted successfully!")
            # Reset the form
            self.reset_form()

            cursor.close()

        except mysql.connector.Error as e:
            print("Error:", e)
            # Handle the error accordingly, such as displaying an error message or logging the error

    def validate_input(self):
        # Get values from UI components
        s_name = self.ui.upload_s_name_2.text()
        s_gender = self.ui.upload_s_gender.currentText()
        s_department = self.ui.upload_s_department.currentText()
        s_address = self.ui.upload_s_address_2.toPlainText()
        s_contact_no = self.ui.upload_s_tel_2.text()
        s_email = self.ui.upload_s_email_2.text()
        s_photo = self.spp_image_name  # Just the image name for validation
        s_g_certificate = self.sgc_image_name  # Just the image name for validation
        s_p_certificate = self.spc_image_name  # Just the image name for validation

        # Validate required fields
        if not s_name.strip():
            self.show_message("Validation Error", "Please enter a name.")
            return False
        elif s_name.isdigit():  # Check if name contains only digits
            self.show_message("Validation Error", "Name cannot contain only numbers.")
            return False
        elif not s_gender:
            self.show_message("Validation Error", "Please select a gender.")
            return False
        elif not s_department:
            self.show_message("Validation Error", "Please select a department.")
            return False
        elif not s_address.strip():
            self.show_message("Validation Error", "Please enter an address.")
            return False
        elif not s_contact_no.strip():
            self.show_message("Validation Error", "Please enter a Contact Number.")
            return False
        elif not s_contact_no.replace("+", "").isdigit():  # Check if contact number contains only digits and "+"
            self.show_message("Validation Error", "Contact Number should contain only numbers and '+'.")
            return False
        elif not s_email.strip():
            self.show_message("Validation Error", "Please enter an Email.")
            return False
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", s_email):  # Validate email format
            self.show_message("Validation Error", "Please enter a valid email address.")
            return False
        elif not s_photo:
            self.show_message("Validation Error", "Please upload a profile picture.")
            return False
        elif not s_g_certificate:
            self.show_message("Validation Error", "Please upload a Grama Niladhari Certificate.")
            return False
        elif not s_p_certificate:
            self.show_message("Validation Error", "Please upload a Police Report.")
            return False

        return True

    def reset_form(self):
        # Reset input fields
        self.ui.upload_s_name_2.clear()
        self.ui.upload_s_gender.setCurrentIndex(0)
        self.ui.upload_s_department.setCurrentIndex(0)
        self.ui.upload_s_address_2.clear()
        self.ui.upload_s_tel_2.clear()
        self.ui.upload_s_email_2.clear()
        self.ui.upload_s_salary_2.clear()

        # Reset image previews
        self.ui.upload_staff_member_pp_2.clear()
        self.ui.view_s_upload_g_certificate.clear()
        self.ui.view_s_upload_p_certificate.clear()

        # Update next ID
        self.next_id = self.get_next_id()
        self.staff_id = "S00" + str(self.next_id)
        self.ui.upload_s_id_2.setText("S00" + str(self.next_id))
