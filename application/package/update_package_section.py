import os
import shutil
import re

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from application.package.ui_update_package import Ui_update_package
import mysql.connector


class UpdatePackage(QMainWindow):
    def __init__(self, p_id):
        super().__init__()

        self.ui = Ui_update_package()
        self.ui.setupUi(self)

        self.p_id = p_id

        # Initialize image file names
        self.pkp_image_name = ""

        #load
        self.display_current_data()

        # button
        self.ui.btn_browser_img_2.clicked.connect(self.upload_package_image)
        self.ui.btn_save_package_2.clicked.connect(self.update_package)

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
            self.pkp_image_name = f"{self.p_id}{extension}"
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

        self.pkp_image_name = ""

    def update_package(self):
        try:
            cursor = self.connection.cursor()

            # Validate input if needed
            if not self.validate_input():
                return

            # Get values from UI components
            p_id = self.p_id
            p_name = self.ui.txt_p_title.text()
            cost_per_person = 1  # Set a default value, you may update this based on UI input
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

            category = ""  # Define the category if needed
            p_image = self.pkp_image_name  # Get the image name from the UI or elsewhere

            # Define the UPDATE query with placeholders
            update_query = """
            UPDATE packages 
            SET p_name = %s, cost_per_person = %s, description = %s, complementary = %s, category = %s, p_image = %s 
            WHERE p_id = %s
            """

            # Execute the query with the values
            cursor.execute(update_query, (
                p_name, cost_per_person, description, complementary, category, p_image, p_id))

            # Commit the transaction
            self.connection.commit()

            print("Package updated successfully!")
            QMessageBox.information(self, "Success", "Package updated successfully!")
            # Reset the form if needed
            # self.reset_form()

            cursor.close()

            self.close()

        except mysql.connector.Error as e:
            print("Error:", e)
            # Handle the error accordingly, such as displaying an error message

    def display_current_data(self):
        try:
            cursor = self.connect_to_mysql().cursor()

            # Fetch data from the packages table for the given package ID
            cursor.execute("SELECT p_id, p_name, cost_per_person, description,"
                           "complementary, p_image FROM packages WHERE p_id = %s", (self.p_id,))

            package_record = cursor.fetchone()  # Assuming there's only one record for the given ID

            if package_record:
                # Extract data from the fetched record
                p_id, p_name, cost_per_person, description, complementary, p_image = package_record

                # Display package details in the UI components
                self.ui.txt_p_id.setText(str(p_id))  # Convert to string if needed
                self.ui.txt_p_title.setText(p_name)
                self.ui.txt_p_description.setPlainText(description)

                try:
                    # Construct the path to the image repository folder relative to the application directory
                    app_folder = os.path.dirname(__file__)
                    image_repo_path = os.path.join(app_folder, "image_repo")

                    # Save the image to the image repository folder with the name = next_id and the correct extension
                    self.pkp_image_name = f"{p_image}"
                    image_dest_path = os.path.join(image_repo_path, self.pkp_image_name)
                    os.makedirs(image_repo_path, exist_ok=True)  # Create folder if it doesn't exist

                    print("Package image uploaded successfully!")
                    # self.show_message("Successful", "Profile picture uploaded successfully!")

                    # Load the image into a QPixmap object
                    pixmap = QPixmap(image_dest_path)

                    # Resize the pixmap to 240x160
                    pixmap = pixmap.scaled(240, 160, Qt.KeepAspectRatio)

                    self.ui.lbl_display_img_2.setPixmap(pixmap)
                except Exception as e:
                    print("Error loading image:", e)

                self.ui.chk_price.setChecked(True)

                # Check the complementary checkboxes based on the fetched data
                complementary_services = complementary.split(", ")
                for service in complementary_services:
                    if service == "FREE WIFI":
                        self.ui.chk_com_wifi.setChecked(True)
                    elif service == "24HR SECURITY":
                        self.ui.chk_com_security.setChecked(True)
                    elif service == "BUTLER SERVICE":
                        self.ui.chk_com_butler_service.setChecked(True)
                    elif service == "CAR PARKING":
                        self.ui.chk_com_car.setChecked(True)
                    elif service == "INFINITY POOL":
                        self.ui.chk_com_pool.setChecked(True)
                    elif service == "24HR SERVICE":
                        self.ui.chk_com_24hr_service.setChecked(True)

            cursor.close()

        except mysql.connector.Error as e:
            print("Error:", e)
            # Handle the error accordingly, such as displaying an error message

