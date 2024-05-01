import os
import shutil
import re

from PySide6 import QtCore
from PySide6.QtCore import Qt, QSize, QDate
from PySide6.QtGui import QPixmap, QPainter, QPainterPath
from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QVBoxLayout, QWidget, QHBoxLayout, QLabel, \
    QPushButton, QTextEdit, QSpinBox, QSpacerItem, QSizePolicy, QGridLayout
from application.cust_package.ui_make_reservation import Ui_make_reservation_form
import mysql.connector


class MakeReservation(QMainWindow):
    def __init__(self, c_id, id, p_id):
        super().__init__()

        self.ui = Ui_make_reservation_form()
        self.ui.setupUi(self)

        self.c_id = c_id
        self.p_id = p_id

        self.id = id

        if self.id > 0:
            print(self.id)
            self.update_packages()
            self.ui.btn_update_reservation.clicked.connect(self.update_reservations)
            self.ui.btn_save_reservation.setEnabled(False)
        else:
            self.ui.btn_update_reservation.setEnabled(False)

        # Initialize image file names
        self.pkp_image_name = ""

        self.ui.txt_cust_id.setText(self.c_id)

        self.display_packages()
        self.ui.calendarWidget.selectionChanged.connect(self.update_date_lineedit)

        self.ui.btn_save_reservation.clicked.connect(self.make_reservations)

        self.ui.cust_no_of_pax.setRange(0, 1000)
        self.ui.cust_no_of_pax.valueChanged.connect(self.update_price_label)

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

    def display_packages(self):
        try:
            cursor = self.connect_to_mysql().cursor()

            cursor.execute("SELECT p_id, p_name, cost_per_person, description, complementary, p_image FROM packages WHERE p_id = %s", (self.p_id,))
            package_records = cursor.fetchall()

            # Clear any existing items in the list widget
            self.clear_list_widget()

            # Get the existing layout or create a new one if none exists
            internal_layout = self.ui.package_img.layout()
            if not internal_layout:
                internal_layout = QVBoxLayout()

            # Iterate over the fetched records and populate the list widget
            for record in package_records:
                # Extract data from the record
                p_id, p_name, cost_per_person, description, complementary, p_image = record

                # Create custom widget to represent the package
                package_widget = QWidget()
                package_layout = QHBoxLayout()
                package_layout.setSpacing(30)

                # Package image
                package_photo = QLabel()
                pixmap = self.load_round_package_image(p_image)
                package_photo.setPixmap(pixmap)
                package_layout.addWidget(package_photo)

                # Package information
                info_widget = QWidget()
                info_layout = QVBoxLayout()

                # Package title and action buttons
                title_widget = QWidget()
                title_layout = QHBoxLayout()
                title_layout.setContentsMargins(0, 0, 0, 0)

                package_title = QLabel(f"{p_name}")
                package_title.setStyleSheet(
                    """
                    QLabel {
                        color: #4C4C6C;
                        font-size: 18px;
                        font-style: normal;
                        font-weight: 700;
                        line-height: normal;
                    }
                    """
                )
                title_layout.addWidget(package_title)

                title_widget.setLayout(title_layout)
                info_layout.addWidget(title_widget)

                # Description
                description_label = QTextEdit(f"{description}")
                row_height = description_label.fontMetrics().lineSpacing()
                max_rows = 5
                max_height = max_rows * row_height
                description_label.setMaximumHeight(max_height)
                description_label.setStyleSheet(
                    """
                    QTextEdit {
                        background: #ffffff;
                        border-radius: 10px;
                        color: #4C4C6C;
                        text-align: justify;
                        font-size: 14px;
                        font-style: normal;
                        font-weight: 400;
                        line-height: normal;
                        padding: 5px;
                    }
                    """
                )
                info_layout.addWidget(description_label)

                # Cost per person
                price_count = QWidget()
                price_count_layout = QHBoxLayout()
                price_count_layout.setContentsMargins(0, 0, 0, 0)

                count = QSpinBox()
                count.setRange(0, 1000)
                count.setStyleSheet(
                    """
                    QSpinBox {
                        border: 1px solid #ccc;
                        border-radius: 5px;
                        padding: 5px;
                        background-color: #fff;
                        min-width: 150px;
                    }
                    """
                )
                price_count_layout.addWidget(count)


                # Services
                grid_layout = QGridLayout()
                complementary_services = complementary.split(", ")
                row = 0
                col = 0
                for index, service in enumerate(complementary_services):
                    service_label = QLabel(f"* {service.strip()}")
                    grid_layout.addWidget(service_label, index // 3, index % 3, alignment=Qt.AlignLeft)
                    col += 1
                    if col == 3:
                        col = 0
                        row += 1

                grid_widget = QWidget()
                grid_widget.setLayout(grid_layout)
                grid_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                info_layout.addWidget(grid_widget)

                horizontal_spacer = QSpacerItem(0, 10, QSizePolicy.Expanding, QSizePolicy.Expanding)
                info_layout.addItem(horizontal_spacer)

                info_widget.setLayout(info_layout)
                package_layout.addWidget(info_widget)
                package_widget.setLayout(package_layout)
                internal_layout.addWidget(package_widget)

            vertical_spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
            internal_layout.addItem(vertical_spacer)
            self.ui.package_img.setLayout(internal_layout)


        except mysql.connector.Error as e:
            print("Error:", e)
            self.show_message("Error", str(e))

    def load_round_package_image(self, p_image):
        current_file_directory = os.path.dirname(__file__)
        parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))
        package_folder = os.path.join(parent_directory, "package")
        image_repo_path = os.path.join(package_folder, "image_repo")
        package_image_path = os.path.join(image_repo_path, p_image)
        pixmap = QPixmap(package_image_path)
        size = QSize(240, 160)
        pixmap = pixmap.scaled(size, Qt.AspectRatioMode.KeepAspectRatio)
        round_pixmap = self.create_round_pixmap(pixmap, size)
        return round_pixmap

    def create_round_pixmap(self, source_pixmap, size, corner_radius=10):
        result_pixmap = QPixmap(size)
        result_pixmap.fill(Qt.transparent)
        painter = QPainter(result_pixmap)
        painter.setRenderHint(QPainter.Antialiasing, True)
        path = QPainterPath()
        path.addRoundedRect(result_pixmap.rect(), corner_radius, corner_radius)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, source_pixmap)
        return result_pixmap

    def clear_list_widget(self):
        layout = self.ui.package_img.layout()
        if layout:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

    def refresh_after_update(self):
        try:
            self.display_packages()
        except Exception as e:
            print("Error refreshing package display:", e)

    def update_price_label(self, num_persons):
        cursor = self.connect_to_mysql().cursor()
        cursor.execute("SELECT max_no_of_pax, cost FROM number_of_pax ORDER BY max_no_of_pax ASC")
        tiers = cursor.fetchall()
        cost_per_person = 100  # Default cost per person
        for max_pax, cost in tiers:
            if num_persons <= max_pax or max_pax == 51:
                cost_per_person = cost
                break
        total_price = num_persons * cost_per_person
        self.ui.cust_tot_price.setText(f"Total Price: Rs. {total_price}")
        cursor.close()

    def update_date_lineedit(self):
        selected_date = self.ui.calendarWidget.selectedDate()
        self.ui.txt_cust_date.setText(selected_date.toString("yyyy-MM-dd"))

    def make_reservations(self):
        c_id = self.ui.txt_cust_id.text()
        fname = self.ui.txt_cust_full_name.text()
        email = self.ui.txt_cust_email.text()
        mobile = self.ui.txt_cust_mobile.text()
        date = self.ui.txt_cust_date.text()
        nop = self.ui.cust_no_of_pax.value()

        if not self.validate_input():
            return

        try:
            # Connect to MySQL database
            connection = self.connect_to_mysql()
            if connection:
                cursor = connection.cursor()

                # Insert reservation details into the cust_reservation table
                sql = "INSERT INTO cust_reservation (c_id, p_id, full_name, email, mobile, no_of_pax, reservation_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = (c_id, self.p_id, fname, email, mobile, nop, date)
                cursor.execute(sql, values)
                connection.commit()

                # Close the cursor and connection
                cursor.close()
                connection.close()

                QMessageBox.information(self, "Success", "Reservation made successfully!")

                # Close the window
                self.close()
            else:
                QMessageBox.warning(self, "Warning", "Error connecting to database.")
        except mysql.connector.Error as e:
            print("Error:", e)
            QMessageBox.warning(self, "Error", f"Failed to make reservation: {e}")

    def validate_input(self):
        c_id = self.ui.txt_cust_id.text()
        fname = self.ui.txt_cust_full_name.text()
        email = self.ui.txt_cust_email.text()
        mobile = self.ui.txt_cust_mobile.text()
        date = self.ui.txt_cust_date.text()
        nop = self.ui.cust_no_of_pax.value()

        if not all([c_id, fname, email, mobile, date]):
            QMessageBox.warning(self, "Warning", "Please fill in all the required fields.")
            return False

        if nop == 0:
            QMessageBox.warning(self, "Warning", "Number of persons cannot be zero.")
            return False

        # Additional validation rules
        if len(fname) > 100:
            QMessageBox.warning(self, "Warning", "Full name exceeds maximum length of 100 characters.")
            return False

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            QMessageBox.warning(self, "Warning", "Invalid email format.")
            return False

        elif not mobile.replace("+", "").isdigit():  # Check if contact number contains only digits and "+"
            self.show_message("Validation Error", "Contact Number should contain only numbers and '+'.")
            return False

        return True

    def update_packages(self):
        try:
            cursor = self.connect_to_mysql().cursor()

            cursor.execute("SELECT id, c_id, p_id, full_name, email, mobile, no_of_pax, reservation_date FROM cust_reservation where id = %s",
                           (self.id,))
            reservation_records = cursor.fetchall()

            for reservation in reservation_records:
                id, c_id, pp_id, full_name, email, mobile, no_of_pax, reservation_date = reservation


            cursor.execute("SELECT p_id, p_name, cost_per_person, description, complementary, p_image FROM packages WHERE p_id = %s", (pp_id,))
            package_records = cursor.fetchall()

            # Clear any existing items in the list widget
            self.clear_list_widget()

            # Get the existing layout or create a new one if none exists
            internal_layout = self.ui.package_img.layout()
            if not internal_layout:
                internal_layout = QVBoxLayout()

            # Iterate over the fetched records and populate the list widget
            for record in package_records:
                # Extract data from the record
                p_id, p_name, cost_per_person, description, complementary, p_image = record

                self.ui.txt_cust_id.setText(c_id)
                self.ui.txt_cust_full_name.setText(full_name)
                self.ui.txt_cust_email.setText(email)
                self.ui.txt_cust_mobile.setText(str(mobile))
                self.ui.txt_cust_date.setText(str(reservation_date))
                self.ui.cust_no_of_pax.setValue(no_of_pax)
                self.update_price_label(no_of_pax)  # Call update_price_label with current value of no_of_pax

                # Connect valueChanged signal of QSpinBox to update_price_label
                self.ui.cust_no_of_pax.valueChanged.connect(self.update_price_label)

                # Inside the update_packages method
                selected_date = QDate.fromString(str(reservation_date), "yyyy-MM-dd")
                self.ui.calendarWidget.setSelectedDate(selected_date)

                # Create custom widget to represent the package
                package_widget = QWidget()
                package_layout = QHBoxLayout()
                package_layout.setSpacing(30)

                # Package image
                package_photo = QLabel()
                pixmap = self.load_round_package_image(p_image)
                package_photo.setPixmap(pixmap)
                package_layout.addWidget(package_photo)

                # Package information
                info_widget = QWidget()
                info_layout = QVBoxLayout()

                # Package title and action buttons
                title_widget = QWidget()
                title_layout = QHBoxLayout()
                title_layout.setContentsMargins(0, 0, 0, 0)

                package_title = QLabel(f"{p_name}")
                package_title.setStyleSheet(
                    """
                    QLabel {
                        color: #4C4C6C;
                        font-size: 18px;
                        font-style: normal;
                        font-weight: 700;
                        line-height: normal;
                    }
                    """
                )
                title_layout.addWidget(package_title)

                title_widget.setLayout(title_layout)
                info_layout.addWidget(title_widget)

                # Description
                description_label = QTextEdit(f"{description}")
                row_height = description_label.fontMetrics().lineSpacing()
                max_rows = 5
                max_height = max_rows * row_height
                description_label.setMaximumHeight(max_height)
                description_label.setStyleSheet(
                    """
                    QTextEdit {
                        background: #ffffff;
                        border-radius: 10px;
                        color: #4C4C6C;
                        text-align: justify;
                        font-size: 14px;
                        font-style: normal;
                        font-weight: 400;
                        line-height: normal;
                        padding: 5px;
                    }
                    """
                )
                info_layout.addWidget(description_label)

                # Cost per person
                price_count = QWidget()
                price_count_layout = QHBoxLayout()
                price_count_layout.setContentsMargins(0, 0, 0, 0)

                count = QSpinBox()
                count.setRange(0, 1000)
                count.setStyleSheet(
                    """
                    QSpinBox {
                        border: 1px solid #ccc;
                        border-radius: 5px;
                        padding: 5px;
                        background-color: #fff;
                        min-width: 150px;
                    }
                    """
                )
                price_count_layout.addWidget(count)


                # Services
                grid_layout = QGridLayout()
                complementary_services = complementary.split(", ")
                row = 0
                col = 0
                for index, service in enumerate(complementary_services):
                    service_label = QLabel(f"* {service.strip()}")
                    grid_layout.addWidget(service_label, index // 3, index % 3, alignment=Qt.AlignLeft)
                    col += 1
                    if col == 3:
                        col = 0
                        row += 1

                grid_widget = QWidget()
                grid_widget.setLayout(grid_layout)
                grid_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                info_layout.addWidget(grid_widget)

                horizontal_spacer = QSpacerItem(0, 10, QSizePolicy.Expanding, QSizePolicy.Expanding)
                info_layout.addItem(horizontal_spacer)

                info_widget.setLayout(info_layout)
                package_layout.addWidget(info_widget)
                package_widget.setLayout(package_layout)
                internal_layout.addWidget(package_widget)

            vertical_spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
            internal_layout.addItem(vertical_spacer)
            self.ui.package_img.setLayout(internal_layout)


        except mysql.connector.Error as e:
            print("Error:", e)
            self.show_message("Error", str(e))

    def update_reservations(self):
        fname = self.ui.txt_cust_full_name.text()
        email = self.ui.txt_cust_email.text()
        mobile = self.ui.txt_cust_mobile.text()
        date = self.ui.txt_cust_date.text()
        nop = self.ui.cust_no_of_pax.value()

        if not self.validate_input():
            return

        try:
            # Connect to MySQL database
            connection = self.connect_to_mysql()
            if connection:
                cursor = connection.cursor()

                # Update reservation details in the cust_reservation table
                sql = "UPDATE cust_reservation SET full_name = %s, email = %s, mobile = %s, no_of_pax = %s, reservation_date = %s WHERE id = %s"
                values = (fname, email, mobile, nop, date, self.id)
                cursor.execute(sql, values)
                connection.commit()

                # Close the cursor and connection
                cursor.close()
                connection.close()

                QMessageBox.information(self, "Success", "Reservation updated successfully!")

                # Refresh the view after updating
                self.refresh_after_update()

                # Close the window
                self.close()
            else:
                QMessageBox.warning(self, "Warning", "Error connecting to database.")

        except mysql.connector.Error as e:
            print("Error:", e)
            QMessageBox.warning(self, "Error", f"Failed to update reservation: {e}")
