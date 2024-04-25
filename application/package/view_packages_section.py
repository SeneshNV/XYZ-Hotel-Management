import os
import shutil
import re

from PySide6.QtCore import QSize
from PySide6.QtGui import Qt, QPixmap, QPainter, QPainterPath
from PySide6.QtWidgets import QWidget, QMessageBox, QVBoxLayout, QLabel, QPushButton, \
    QListWidget, QListWidgetItem, QHBoxLayout, QSpacerItem, QSizePolicy, QLineEdit, QTextEdit, QComboBox, QFileDialog, \
    QSpinBox
from application.package.ui_view_package import Ui_view_package_form
import mysql.connector

class ViewPackage(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_view_package_form()
        self.ui.setupUi(self)  # Set up the UI components

        # Remove title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Display packages when the widget is initialized
        self.display_packages()


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

            # Fetch data from the packages table
            cursor.execute("SELECT p_id, p_name, cost_per_person, description,"
                           "complementary, p_image FROM packages")

            package_records = cursor.fetchall()

            # Clear any existing items in the list widget
            self.clear_list_widget()

            # Create a vertical layout for the list widget's internal widget
            internal_layout = QVBoxLayout()

            # Iterate over the fetched records and populate the list widget
            for record in package_records:
                # Extract data from the record
                p_id, p_name, cost_per_person, description, complementary, \
                    p_image = record

                # Create custom widget to represent the package
                package_widget = QWidget()
                package_layout = QHBoxLayout()

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

                update_button = QPushButton("Update")
                update_button.setStyleSheet(
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
                update_button.setFixedWidth(100)
                update_button.clicked.connect(lambda state, id=p_id: self.update_package(id))
                title_layout.addWidget(update_button)

                delete_button = QPushButton("Delete")
                delete_button.setStyleSheet(
                    """
                    QPushButton {
                        background-color: #C79C99;
                        color: #000;
                        padding : 5px 2px;
                        margin-top: 4px;
                        border-radius: 10px;
                    }

                    QPushButton:hover {
                        background-color: #AE544F;
                    }
                    """
                )
                delete_button.setFixedWidth(100)
                delete_button.clicked.connect(lambda state, id=p_id: self.delete_package(id))
                title_layout.addWidget(delete_button)

                title_widget.setLayout(title_layout)
                info_layout.addWidget(title_widget)

                # Description
                description_label = QTextEdit(f"{description}")
                info_layout.addWidget(description_label)

                # Cost per person
                cost_label = QLabel(f"Cost per Person: {cost_per_person}")
                info_layout.addWidget(cost_label)

                # Complementary services
                complementary_label = QLabel(f"Complementary: {complementary}")
                info_layout.addWidget(complementary_label)

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
        # Load the package image
        app_folder = os.path.dirname(__file__)
        image_repo_path = os.path.join(app_folder, "image_repo")
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

    def update_package(self, package_id):
        # Implement package update functionality here
        pass

    def delete_package(self, package_id):
        # Implement package deletion functionality here
        pass
