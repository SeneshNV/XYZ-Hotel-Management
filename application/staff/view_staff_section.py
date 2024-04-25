import os
import shutil
import re

from PySide6.QtCore import QSize
from PySide6.QtGui import Qt, QPixmap, QPainter, QPainterPath
from PySide6.QtWidgets import QWidget, QMessageBox, QVBoxLayout, QLabel, QPushButton, \
    QListWidget, QListWidgetItem, QHBoxLayout, QSpacerItem, QSizePolicy, QLineEdit, QTextEdit, QComboBox, QFileDialog
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
        self.display_staff()

        # Connect buttons to set_editable method
        self.connect_edit_buttons()

        self.s_salary = 0

        self.current_staff_id = None
        self.spp_image_name = None

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

    def display_staff(self):
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
                layout = QHBoxLayout()  # Horizontal layout for the custom widget

                # 1. Profile picture
                label_photo = QLabel()
                pixmap = self.load_round_profile_pic(s_photo)
                label_photo.setPixmap(pixmap)  # Set rounded pixmap
                layout.addWidget(label_photo, alignment=Qt.AlignVCenter)

                # 2. ID and name
                widget_id_name = QWidget()
                layout_id_name = QVBoxLayout()  # Vertical layout for the ID and name

                label_id = QLabel(f"{staff_id}")
                layout_id_name.addWidget(label_id)

                label_name = QLabel(f"{s_name}")
                label_name.setStyleSheet(
                    """
                    QLabel {
                        color: #4C4C6C;
                        font-size: 14px;
                        font-style: normal;
                        font-weight: 700;
                        line-height: normal;
                    }
                    """
                )
                layout_id_name.addWidget(label_name)

                # Set layout for the ID and name widget
                widget_id_name.setLayout(layout_id_name)
                layout.addWidget(widget_id_name)

                # Add a horizontal spacer to push the view button to the right
                spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
                layout.addItem(spacer)

                # 3. View button
                view_button = QPushButton("View")
                view_button.setStyleSheet(
                    """
                    QPushButton {
                        background-color: #4C4C6C;
                        color: #ffffff;
                        padding : 5px 2px;
                        margin-top: 4px;
                        border-radius: 10px;
                    }

                    QPushButton:hover {
                        background-color: #AE544F;
                    }
                    """
                )
                view_button.setFixedWidth(100)

                from functools import partial
                view_button.clicked.connect(partial(self.view_staff, staff_id))

                layout.addWidget(view_button)

                # Set layout for the custom widget
                widget.setLayout(layout)

                # Add the custom widget to the internal layout
                internal_layout.addWidget(widget)

            vertical_spacer = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
            internal_layout.addItem(vertical_spacer)

            self.ui.staff_member_list.widget().setLayout(internal_layout)

            cursor.close()

        except mysql.connector.Error as e:
            print("Error:", e)
            self.show_message("Error", str(e))

    def load_round_profile_pic(self, s_photo):
        # Load the profile picture
        app_folder = os.path.dirname(__file__)
        image_repo_path = os.path.join(app_folder, "image_repo")
        user_profile_pic_path = os.path.join(image_repo_path, s_photo)
        pixmap = QPixmap(user_profile_pic_path)

        # Resize pixmap to a uniform size
        size = QSize(50, 50)
        pixmap = pixmap.scaled(size, Qt.AspectRatioMode.KeepAspectRatio)

        # Create a round pixmap
        round_pixmap = self.create_round_pixmap(pixmap, size)

        return round_pixmap

    def create_round_pixmap(self, source_pixmap, size):
        result_pixmap = QPixmap(size)
        result_pixmap.fill(Qt.transparent)

        painter = QPainter(result_pixmap)
        painter.setRenderHint(QPainter.Antialiasing, True)

        path = QPainterPath()
        path.addRoundedRect(result_pixmap.rect(), size.width() / 2, size.height() / 2)

        painter.setClipPath(path)
        painter.drawPixmap(0, 0, source_pixmap)

        return result_pixmap

    def clear_list_widget(self):
        # Clear the internal layout of the list widget
        layout = self.ui.staff_member_list.widget().layout()
        if layout:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

    def delete_staff(self):
        try:
            cursor = self.connection.cursor()

            # Execute the DELETE query
            cursor.execute("DELETE FROM staff WHERE staff_id = %s", (self.s_id,))

            # Commit the transaction
            self.connection.commit()

            print("Staff deleted successfully!")
            QMessageBox.information(self, "Success", "Staff deleted successfully!")

            # Optionally, you might want to clear the UI fields after deletion
            self.clear_ui_fields()
            cursor.close()

        except mysql.connector.Error as e:
            print("Error:", e)
            # Handle the error accordingly, such as displaying an error message or logging the error

    def clear_ui_fields(self):
        # Clear all UI fields
        self.ui.view_s_id.clear()
        self.ui.view_s_name.clear()

        self.ui.view_s_address.clear()
        self.ui.view_s_tel.clear()
        self.ui.view_s_email.clear()
        self.ui.view_s_salary.clear()
        self.ui.staff_member_pp.clear()

    def view_staff(self, s_id):
        cursor = self.connect_to_mysql().cursor()
        self.s_id = s_id
        # Fetch data from the staff table
        cursor.execute("SELECT staff_id, s_name, s_photo, s_gender, s_department, s_address, s_contact_no, s_email, "
                       "s_salary FROM staff where staff_id = %s", (self.s_id,))
        staff_data = cursor.fetchall()

        for s_details in staff_data:
            # Extract data from the record
            (view_s_id, view_s_name, staff_member_pp, view_s_gender, view_s_department, view_s_address, view_s_tel,
             view_s_email, view_s_salary) = s_details

        self.ui.view_s_id.setText(view_s_id)
        self.ui.view_s_name.setText(view_s_name)
        # Set ComboBox values
        self.ui.view_s_gender.setCurrentText(view_s_gender)
        self.ui.view_s_department.setCurrentText(view_s_department)

        self.ui.view_s_address.setPlainText(view_s_address)  # Correct typo in method name
        self.ui.view_s_tel.setText(view_s_tel)
        self.ui.view_s_email.setText(view_s_email)
        self.ui.view_s_salary.setText("Rs." + str(view_s_salary) + ".00")


        self.ui.view_s_gender.setEnabled(False)
        self.ui.view_s_department.setEnabled(False)

        app_folder = os.path.dirname(__file__)
        image_repo_path = os.path.join(app_folder, "image_repo")
        user_profile_pic_path = os.path.join(image_repo_path, staff_member_pp)
        pixmap = QPixmap(user_profile_pic_path)

        # Resize pixmap to a uniform size
        size = QSize(120, 120)
        pixmap = pixmap.scaled(size, Qt.AspectRatioMode.KeepAspectRatio)
        self.ui.staff_member_pp.setPixmap(pixmap)

        # Connect the delete button signal
        self.ui.view_s_delete.clicked.connect(self.delete_staff)

        self.current_staff_id = s_id
        cursor.close()

    def connect_edit_buttons(self):
        self.ui.name_edit.clicked.connect(lambda: self.edit_button_clicked(self.ui.view_s_name))
        self.ui.gender_edit.clicked.connect(lambda: self.edit_button_clicked(self.ui.view_s_gender))
        self.ui.dep_edit.clicked.connect(lambda: self.edit_button_clicked(self.ui.view_s_department))
        self.ui.address_edit.clicked.connect(lambda: self.edit_button_clicked(self.ui.view_s_address))
        self.ui.tel_edit.clicked.connect(lambda: self.edit_button_clicked(self.ui.view_s_tel))
        self.ui.email_edit.clicked.connect(lambda: self.edit_button_clicked(self.ui.view_s_email))

        self.ui.pp_edit.clicked.connect(self.upload_staff_image)

        # Connect the view_s_update button to the update_staff method
        self.ui.view_s_update.clicked.connect(self.update_staff)

        # Initialize a variable to keep track of the salary update connection
        self.salary_update_connection = None

    def edit_button_clicked(self, widget):
        self.set_editable(widget, False)
        self.setup_salary_update()

    def setup_salary_update(self):
        # Disconnect the previous connection if it exists
        if self.salary_update_connection:
            self.ui.view_s_department.currentTextChanged.disconnect(self.salary_update_connection)

        # Establish a new connection and store the connection object
        self.salary_update_connection = self.ui.view_s_department.currentTextChanged.connect(self.update_salary)

    def set_editable(self, widget, isReadOnly):
        if isinstance(widget, (QLineEdit, QTextEdit)):
            widget.setReadOnly(isReadOnly)
        elif isinstance(widget, QComboBox):
            widget.setEnabled(not isReadOnly)

        # Enable or disable the update button based on the editing state
        self.ui.view_s_update.setEnabled(not isReadOnly)

    def update_staff(self):
        if self.current_staff_id is None:
            # No staff member is currently being viewed, so do nothing
            return


        # Retrieve updated data
        updated_name = self.ui.view_s_name.text()
        updated_gender = self.ui.view_s_gender.currentText()
        updated_department = self.ui.view_s_department.currentText()
        updated_address = self.ui.view_s_address.toPlainText()
        updated_tel = self.ui.view_s_tel.text()
        updated_email = self.ui.view_s_email.text()



        updated_salary = int(self.calculate_salary(updated_department).replace('Rs.', '').replace(',', ''))

        # Update the database with the new values for the currently viewed staff member
        connection = self.connect_to_mysql()
        cursor = connection.cursor()
        cursor.execute("UPDATE staff SET s_name = %s, s_gender = %s, s_department = %s, s_address = %s, "
                       "s_contact_no = %s, s_email = %s, s_salary = %s WHERE staff_id = %s",
                       (updated_name, updated_gender, updated_department, updated_address, updated_tel,
                        updated_email, updated_salary, self.current_staff_id))
        connection.commit()
        cursor.close()

        # Inform the user about the update
        QMessageBox.information(self, "Success", "Staff information updated successfully.")
        self.clear_ui_fields()  # Clear UI fields after update
        self.current_staff_id = None  # Reset current_staff_id after update
        self.spp_image_name = None

    def update_salary(self):
        # Get the current department selected by the user
        department = self.ui.view_s_department.currentText()

        # Calculate the salary based on the selected department
        salary = self.calculate_salary(department)

        self.s_salary = salary

        # Update the salary field in the UI
        self.ui.view_s_salary.setText(str(salary))

        return salary

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

    def upload_staff_image(self):
        if self.current_staff_id is None:
            QMessageBox.warning(self, "Warning", "No staff member is currently being viewed.")
            return

        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Upload Image", "", "Images (*.png *.jpg *.bmp);;All Files (*)",
                                                  options=options)
        if filename:
            _, extension = os.path.splitext(filename)
            app_folder = os.path.dirname(__file__)
            image_repo_path = os.path.join(app_folder, "image_repo")
            self.spp_image_name = f"{self.s_id}{extension}"
            image_dest_path = os.path.join(image_repo_path, self.spp_image_name)
            os.makedirs(image_repo_path, exist_ok=True)
            shutil.copy(filename, image_dest_path)
            print("Profile picture uploaded successfully!")
            pixmap = QPixmap(image_dest_path)
            pixmap = pixmap.scaled(120, 120, Qt.KeepAspectRatio)
            self.ui.staff_member_pp.setPixmap(pixmap)

            s_photo = self.spp_image_name
            connection = self.connect_to_mysql()
            cursor = connection.cursor()
            cursor.execute("UPDATE staff SET s_photo = %s WHERE staff_id = %s", (s_photo, self.current_staff_id))
            connection.commit()
            cursor.close()
            self.spp_image_name = None


