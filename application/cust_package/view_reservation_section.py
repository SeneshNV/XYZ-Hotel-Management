import os
import shutil
import re

from PySide6.QtCore import QSize
from PySide6.QtGui import Qt, QPixmap, QPainter, QPainterPath
from PySide6.QtWidgets import QWidget, QMessageBox, QVBoxLayout, QLabel, QPushButton, \
    QListWidget, QListWidgetItem, QHBoxLayout, QSpacerItem, QSizePolicy, QLineEdit, QTextEdit, QComboBox, QFileDialog, \
    QSpinBox, QGridLayout
from application.cust_package.ui_view_reservation import Ui_view_reservation_form
import mysql.connector

class ViewReservation(QWidget):
    def __init__(self, c_id):
        super().__init__()

        self.c_id = c_id
        print("open my reservations")

        self.ui = Ui_view_reservation_form()
        self.ui.setupUi(self)  # Set up the UI components

        # Remove title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.view_my_reservation()

        self.ui.update_this_list.clicked.connect(self.view_my_reservation)

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

    def view_my_reservation(self):
        print("view_my_reservation")
        try:
            cursor = self.connect_to_mysql().cursor()

            cursor.execute("SELECT id, c_id, p_id, no_of_pax, reservation_date FROM cust_reservation where c_id = %s",
                           (self.c_id,))
            reservation_records = cursor.fetchall()

            # Clear any existing items in the list widget
            self.clear_list_widget()

            reservation_layout_final = self.ui.package_list.widget().layout()
            if not reservation_layout_final:
                reservation_layout_final = QVBoxLayout()

            for reservation in reservation_records:
                id,c_id, p_id, no_of_pax, reservation_date = reservation

                cursor.execute("SELECT p_name, cost_per_person FROM packages where p_id = %s", (p_id,))
                package_record = cursor.fetchone()

                if package_record:
                    p_name, cost_per_person = package_record
                else:
                    p_name = "Unknown"
                    cost_per_person = "Unknown"

                # Calculate total price
                tot_cost = self.calculate_total_cost(cursor, no_of_pax)

                # Create widgets to display reservation details
                reservation_widget = QWidget()
                reservation_layout = QVBoxLayout()  # Use QVBoxLayout for a vertical list style
                reservation_layout.setSpacing(0)

                # Set background color and fixed height
                reservation_widget.setStyleSheet(
                    """
                    background-color: #f0f0f0;
                    max-width:650px;
                    border-radius:10px;
                    """
                )

                # First row: package information
                package_info_widget = QWidget()
                package_info_layout = QHBoxLayout()


                # First column: package details
                col1_widget = QWidget()
                col1_layout = QVBoxLayout()

                select_pck_name = QLabel()
                select_pck_name.setStyleSheet(
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
                select_pck_name.setText(p_name)
                col1_layout.addWidget(select_pck_name)

                select_pck_date = QLabel(str(reservation_date))
                select_pck_date.setStyleSheet(
                    """
                    QLabel {
                        color: #4C4C6C;
                        font-size: 14px;
                        font-style: normal;
                        font-weight: 600;
                        line-height: normal;
                    }
                    """
                )
                col1_layout.addWidget(select_pck_date)

                select_pck_nop = QLabel("No. of Pax: " + str(no_of_pax))
                col1_layout.addWidget(select_pck_nop)

                col1_widget.setLayout(col1_layout)
                package_info_layout.addWidget(col1_widget)

                # Second column: total price
                col2_widget = QWidget()
                col2_layout = QVBoxLayout()

                select_pck_price_label = QLabel("Total Price")
                select_pck_price_label.setStyleSheet("font-weight: bold;")
                col2_layout.addWidget(select_pck_price_label)

                select_pck_price = QLabel("Rs. " + str(tot_cost))  # Add currency symbol
                select_pck_price.setStyleSheet(
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
                col2_layout.addWidget(select_pck_price)

                col2_widget.setLayout(col2_layout)
                package_info_layout.addWidget(col2_widget)

                package_info_widget.setLayout(package_info_layout)
                reservation_layout.addWidget(package_info_widget)

                # Second row: buttons
                button_widget = QWidget()
                button_layout = QHBoxLayout()

                # Add horizontal spacer before buttons
                button_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
                button_layout.addItem(button_spacer)

                edit_btn = QPushButton("Edit Reservation")
                edit_btn.setStyleSheet(
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
                from functools import partial
                edit_btn.clicked.connect(partial(self.edit_reservations, id, p_id))
                button_layout.addWidget(edit_btn)

                cancel_btn = QPushButton("Cancel Reservation")
                cancel_btn.setStyleSheet(
                    """
                    QPushButton {
                        background-color: #AE544F;
                        color: #ffffff;
                        padding : 5px 20px;
                        margin-top: 4px;
                        border-radius: 10px;
                    }

                    QPushButton:hover {
                        background-color: #000;
                    }
                    """
                )
                from functools import partial
                cancel_btn.clicked.connect(partial(self.del_reservations, id))
                button_layout.addWidget(cancel_btn)

                button_widget.setLayout(button_layout)
                reservation_layout.addWidget(button_widget)

                # Add vertical spacer after reservation layout
                vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
                reservation_layout.addItem(vertical_spacer)

                reservation_widget.setLayout(reservation_layout)

                # Add the custom widget to the internal layout
                reservation_layout_final.addWidget(reservation_widget)

            # Add vertical spacer to layout
            vertical_spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
            reservation_layout_final.addItem(vertical_spacer)

            # Set internal layout for package list
            self.ui.package_list.widget().setLayout(reservation_layout_final)

            cursor.close()
            self.connection.close()


        except mysql.connector.Error as e:
            print("Error accessing MySQL:", e)
            self.show_message("Error", "Failed to access database.")

    def calculate_total_cost(self, cursor, no_of_pax):
        num_persons = no_of_pax  # Assuming no_of_pax is already an integer
        try:
            cursor.execute("SELECT max_no_of_pax, cost FROM number_of_pax ORDER BY max_no_of_pax ASC")
            tiers = cursor.fetchall()

            # Find the applicable price tier
            cost_per_person = 100  # Default cost per person
            for max_pax, cost in tiers:
                if num_persons <= max_pax or max_pax == 51:
                    cost_per_person = cost
                    break

            # Calculate total price
            total_price = num_persons * cost_per_person
            return total_price
        except mysql.connector.Error as e:
            print("Error accessing MySQL:", e)
            self.show_message("Error", "Failed to access database.")
            return None


    def clear_list_widget(self):
        # Clear the internal layout of the list widget
        layout = self.ui.package_list.widget().layout()
        if layout:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

    def edit_reservations(self, id, p_id):
        from application.cust_package.make_reservation_section import MakeReservation
        self.make_reser = MakeReservation(self.c_id, id, p_id)
        self.make_reser.show()

    def del_reservations(self, reservation_id):
        # Confirmation dialog
        confirmation = QMessageBox()
        confirmation.setIcon(QMessageBox.Question)
        confirmation.setWindowTitle("Confirm")
        confirmation.setText("Are you sure you want to cancel this reservation?")

        # Add "Yes" button
        yes_button = confirmation.addButton("Yes", QMessageBox.YesRole)
        confirmation.setDefaultButton(yes_button)

        # Add "No" button
        no_button = confirmation.addButton("No", QMessageBox.NoRole)

        confirmation.exec()

        # Check which button was clicked
        if confirmation.clickedButton() == yes_button:
            try:
                # Connect to the database
                connection = self.connect_to_mysql()
                if not connection:
                    return

                cursor = connection.cursor()

                # Execute the DELETE query
                cursor.execute("DELETE FROM cust_reservation WHERE id = %s", (reservation_id,))
                connection.commit()

                cursor.close()
                connection.close()

                # Refresh the reservation list after deletion
                self.view_my_reservation()

                QMessageBox.information(self, "Success", "Reservation canceled successfully!")

            except mysql.connector.Error as e:
                print("Error:", e)
                QMessageBox.warning(self, "Error", f"Failed to cancel reservation: {e}")
