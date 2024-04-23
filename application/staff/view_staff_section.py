import os
import shutil
import re

from PySide6.QtCore import QSize
from PySide6.QtGui import Qt, QPixmap
from PySide6.QtWidgets import QWidget, QMessageBox, QVBoxLayout, QLabel, QPushButton, \
    QListWidget, QListWidgetItem, QHBoxLayout
from application.staff.ui_view_staff import Ui_view_staff_form
import mysql.connector

class ViewStaff(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_view_staff_form()
        self.ui.setupUi(self)  # Set up the UI components

        # Remove title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Load staff data
        self.view_staff()

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

    def view_staff(self):
        try:
            cursor = self.connect_to_mysql().cursor()

            # Fetch data from the staff table
            cursor.execute("SELECT staff_id, s_name, s_photo FROM staff")
            staff_records = cursor.fetchall()

            # Clear any existing items in the list widget
            self.clear_list_widget()

            # Create a vertical layout for the list widget's internal widget
            internal_layout = QVBoxLayout()

            # Iterate over the fetched records and populate the list widget
            for record in staff_records:
                # Extract data from the record
                staff_id, s_name, s_photo = record

                # Create custom widget to represent the staff member
                widget = QWidget()
                layout = QHBoxLayout()  # Vertical layout for the custom widget

                # 1. Profile picture
                app_folder = os.path.dirname(__file__)
                image_repo_path = os.path.join(app_folder, "image_repo")
                user_profile_pic_path = os.path.join(image_repo_path, s_photo)
                pixmap = QPixmap(user_profile_pic_path)  # Load the profile picture
                label_photo = QLabel()
                label_photo.setPixmap(pixmap.scaled(50, 50, Qt.KeepAspectRatio))  # Resize pixmap
                layout.addWidget(label_photo)

                # 2. ID and name
                widget_id_name = QWidget()
                layout_id_name = QVBoxLayout()  # Vertical layout for the ID and name

                label_id = QLabel(f"ID: {staff_id}")
                layout_id_name.addWidget(label_id)

                label_name = QLabel(f"Name: {s_name}")
                layout_id_name.addWidget(label_name)

                # Set layout for the ID and name widget
                widget_id_name.setLayout(layout_id_name)
                layout.addWidget(widget_id_name)

                # 3. View button
                view_button = QPushButton("View")
                layout.addWidget(view_button)

                # Set layout for the custom widget
                widget.setLayout(layout)

                # Add the custom widget to the internal layout
                internal_layout.addWidget(widget)

            # Set the internal layout for the list widget
            self.ui.staff_member_list.widget().setLayout(internal_layout)

        except mysql.connector.Error as e:
            print("Error:", e)
            self.show_message("Error", str(e))

    def clear_list_widget(self):
        # Clear the internal layout of the list widget
        layout = self.ui.staff_member_list.widget().layout()
        if layout:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
