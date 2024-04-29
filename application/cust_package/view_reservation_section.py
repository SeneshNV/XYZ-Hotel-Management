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

        self.ui = Ui_view_reservation_form()
        self.ui.setupUi(self)  # Set up the UI components

        # Remove title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)