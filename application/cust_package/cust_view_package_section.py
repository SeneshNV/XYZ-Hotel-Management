import os
import shutil
import re

from PySide6.QtCore import QSize
from PySide6.QtGui import Qt, QPixmap, QPainter, QPainterPath
from PySide6.QtWidgets import QWidget, QMessageBox, QVBoxLayout, QLabel, QPushButton, \
    QListWidget, QListWidgetItem, QHBoxLayout, QSpacerItem, QSizePolicy, QLineEdit, QTextEdit, QComboBox, QFileDialog, \
    QSpinBox, QGridLayout
from application.cust_package.ui_view_package import Ui_view_package_form
import mysql.connector

class ViewPackage(QWidget):
    def __init__(self, c_id):
        super().__init__()

        self.c_id = c_id

        self.ui = Ui_view_package_form()
        self.ui.setupUi(self)  # Set up the UI components

        # Remove title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Display packages when the widget is initialized
        self.display_packages()

        self.ui.btn_search.clicked.connect(self.display_packages)

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

            search_text = self.ui.txt_search.text().strip()

            # If search text is empty, display all staff
            if not search_text:
                # Fetch data from the packages table
                cursor.execute("SELECT p_id, p_name, cost_per_person, description,"
                               "complementary, p_image FROM packages")

                package_records = cursor.fetchall()
            else:
                cursor.execute("SELECT p_id, p_name, cost_per_person, description,"
                               "complementary, p_image FROM packages WHERE p_name LIKE %s",
                               ('%' + search_text + '%',))

                package_records = cursor.fetchall()



            # Clear any existing items in the list widget
            self.clear_list_widget()

            # Get the existing layout or create a new one if none exists
            internal_layout = self.ui.package_list.widget().layout()
            if not internal_layout:
                internal_layout = QVBoxLayout()

            # Iterate over the fetched records and populate the list widget
            for record in package_records:
                # Extract data from the record
                p_id, p_name, cost_per_person, description, complementary, \
                    p_image = record

                # Create custom widget to represent the package
                package_widget = QWidget()
                package_layout = QHBoxLayout()
                package_layout.setSpacing(50)

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
                        font-weight: 500;
                        line-height: normal;
                    }
                    """
                )
                title_layout.addWidget(package_title)

                update_button = QPushButton("Make Reservations")
                update_button.setStyleSheet(
                    """
                    QPushButton {
                        background-color: #3474D4;
                        color: #ffffff;
                        padding : 5px 20px;
                        margin-top: 4px;
                        border-radius: 10px;
                    }

                    QPushButton:hover {
                        background-color: #17396D;
                    }
                    """
                )
                update_button.setFixedWidth(150)
                from functools import partial
                update_button.clicked.connect(partial(self.make_reservations, p_id))
                title_layout.addWidget(update_button)

                title_widget.setLayout(title_layout)
                info_layout.addWidget(title_widget)

                # Description
                description_label = QTextEdit(f"{description}")
                row_height = description_label.fontMetrics().lineSpacing()  # Get the height of one row of text
                max_rows = 5  # Set the maximum number of rows
                max_height = max_rows * row_height  # Calculate the maximum height
                description_label.setMaximumHeight(max_height)  # Set the maximum height of the QTextEdit

                description_label.setStyleSheet(
                    """
                    QTextEdit {
                        background: #F4F4F4;
                        border-radius: 10px;color: #4C4C6C;
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
                # 2.3 person count

                price_count = QWidget()
                price_count_layout = QHBoxLayout()
                price_count_layout.setContentsMargins(0, 0, 0, 0)

                count = QSpinBox()

                # Set the range from 1 to 1000
                count.setRange(0, 1000)

                # Apply custom style using a style sheet
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
                price = QLabel("Total Price : ")
                price.setStyleSheet(
                    """
                    QLabel {
                        color: #000;
                        font-size: 14px;
                        font-style: normal;
                        font-weight: 500;
                        line-height: normal;
                    }
                    """
                )
                price_count_layout.addWidget(price)

                count.valueChanged.connect(
                    lambda value, counts=count, prices=price: self.update_price_label(counts, prices))

                # Add a horizontal spacer
                spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
                price_count_layout.addItem(spacer)

                price_count.setLayout(price_count_layout)
                info_layout.addWidget(price_count)

                #4 services

                # Create a grid layout
                grid_layout = QGridLayout()

                # Split the complementary services
                complementary_services = complementary.split(", ")

                # Add bullet labels to the grid layout
                row = 0
                col = 0
                for index, service in enumerate(complementary_services):
                    service_label = QLabel(f"* {service.strip()}")
                    grid_layout.addWidget(service_label, index // 3, index % 3, alignment=Qt.AlignLeft)

                    # Move to the next column
                    col += 1

                    # Move to the next row if the column reaches the third column
                    if col == 3:
                        col = 0
                        row += 1

                # Create a widget to contain the grid layout
                grid_widget = QWidget()
                grid_widget.setLayout(grid_layout)

                # Set horizontal stretch factor to make the grid expand
                grid_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

                # Add the grid widget to your main layout
                info_layout.addWidget(grid_widget)

                # Add a horizontal spacer
                horizontal_spacer = QSpacerItem(0, 10, QSizePolicy.Expanding, QSizePolicy.Expanding)
                info_layout.addItem(horizontal_spacer)

                info_widget.setLayout(info_layout)
                package_layout.addWidget(info_widget)

                package_widget.setLayout(package_layout)

                # Add the custom widget to the internal layout
                internal_layout.addWidget(package_widget)

            # Add vertical spacer to layout
            vertical_spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
            internal_layout.addItem(vertical_spacer)

            # Set internal layout for package list
            self.ui.package_list.widget().setLayout(internal_layout)

        except mysql.connector.Error as e:
            print("Error:", e)
            self.show_message("Error", str(e))

    def load_round_package_image(self, p_image):
        # Get the directory name of the current file
        current_file_directory = os.path.dirname(__file__)

        # Navigate back one directory from the current directory
        parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

        # Access the 'package' directory
        package_folder = os.path.join(parent_directory, "package")

        # Access the 'image_repo' folder within the 'package' directory
        image_repo_path = os.path.join(package_folder, "image_repo")

        # Construct the path to the package image
        package_image_path = os.path.join(image_repo_path, p_image)

        # Load the package image
        pixmap = QPixmap(package_image_path)

        # Resize pixmap to a uniform size
        size = QSize(240, 160)
        pixmap = pixmap.scaled(size, Qt.AspectRatioMode.KeepAspectRatio)

        # Create a round pixmap with rounded corners
        round_pixmap = self.create_round_pixmap(pixmap, size)

        return round_pixmap

    def create_round_pixmap(self, source_pixmap, size, corner_radius=10):
        result_pixmap = QPixmap(size)
        result_pixmap.fill(Qt.transparent)

        painter = QPainter(result_pixmap)
        painter.setRenderHint(QPainter.Antialiasing, True)

        # Create rounded rectangle path
        path = QPainterPath()
        path.addRoundedRect(result_pixmap.rect(), corner_radius, corner_radius)

        painter.setClipPath(path)
        painter.drawPixmap(0, 0, source_pixmap)

        return result_pixmap

    def clear_list_widget(self):
        # Clear the internal layout of the list widget
        layout = self.ui.package_list.widget().layout()
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


    def update_price_label(self, count, price_label):
        # Fetch the current number of persons
        num_persons = count.value()

        # Fetch data from the number_of_pax table
        cursor = self.connect_to_mysql().cursor()
        cursor.execute("SELECT max_no_of_pax, cost FROM number_of_pax ORDER BY max_no_of_pax ASC")
        tiers = cursor.fetchall()

        # Find the applicable price tier
        # Find the applicable price tier
        cost_per_person = 100  # Default cost per person
        for max_pax, cost in tiers:
            if num_persons <= max_pax or max_pax == 51:
                cost_per_person = cost
                break

        # Calculate total price
        total_price = num_persons * cost_per_person

        # Update the price label
        price_label.setText(f"Total Price: Rs. {total_price}")

        cursor.close()


    def make_reservations(self, p_id):
        id = 0
        from application.cust_package.make_reservation_section import MakeReservation
        self.make_reser = MakeReservation(self.c_id, id, p_id)
        self.make_reser.show()