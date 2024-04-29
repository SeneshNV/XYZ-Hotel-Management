# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'make_reservationmmHzmT.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_make_reservation_form(object):
    def setupUi(self, make_reservation_form):
        if not make_reservation_form.objectName():
            make_reservation_form.setObjectName(u"make_reservation_form")
        make_reservation_form.resize(825, 679)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(make_reservation_form.sizePolicy().hasHeightForWidth())
        make_reservation_form.setSizePolicy(sizePolicy)
        make_reservation_form.setMinimumSize(QSize(825, 630))
        make_reservation_form.setMaximumSize(QSize(825, 679))
        make_reservation_form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(make_reservation_form)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.package_img = QFrame(self.centralwidget)
        self.package_img.setObjectName(u"package_img")
        self.package_img.setMinimumSize(QSize(0, 230))
        self.package_img.setStyleSheet(u"background-color: rgb(238, 238, 238);")
        self.package_img.setFrameShape(QFrame.StyledPanel)
        self.package_img.setFrameShadow(QFrame.Raised)
        self.package_img.setLineWidth(0)

        self.verticalLayout.addWidget(self.package_img)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 440))
        self.scrollArea.setStyleSheet(u"border:none;\n"
"background-color: rgb(255, 255, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 825, 440))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, -1, -1, -1)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 700 14pt \"SF Pro Display\";")

        self.verticalLayout_2.addWidget(self.label_3)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setContentsMargins(9, -1, -1, -1)
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(80, 0))
        self.label_12.setMaximumSize(QSize(80, 16777215))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_12)

        self.txt_cust_id = QLineEdit(self.frame_2)
        self.txt_cust_id.setObjectName(u"txt_cust_id")
        self.txt_cust_id.setMaximumSize(QSize(180, 16777215))
        self.txt_cust_id.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #404040;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.txt_cust_id)

        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_13)

        self.txt_cust_full_name = QLineEdit(self.frame_2)
        self.txt_cust_full_name.setObjectName(u"txt_cust_full_name")
        self.txt_cust_full_name.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #404040;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.txt_cust_full_name)

        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_14)

        self.txt_cust_email = QLineEdit(self.frame_2)
        self.txt_cust_email.setObjectName(u"txt_cust_email")
        self.txt_cust_email.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #404040;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.txt_cust_email)

        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_15)

        self.txt_cust_mobile = QLineEdit(self.frame_2)
        self.txt_cust_mobile.setObjectName(u"txt_cust_mobile")
        self.txt_cust_mobile.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #404040;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.txt_cust_mobile)

        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_16)

        self.cust_no_of_pax = QSpinBox(self.frame_2)
        self.cust_no_of_pax.setObjectName(u"cust_no_of_pax")
        self.cust_no_of_pax.setMaximumSize(QSize(100, 30))
        self.cust_no_of_pax.setStyleSheet(u"font: 12pt \"SF Pro Display\";\n"
"background-color: rgb(217, 217, 217);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"    padding: 8px 16px; ")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.cust_no_of_pax)

        self.cust_tot_price = QLabel(self.frame_2)
        self.cust_tot_price.setObjectName(u"cust_tot_price")
        self.cust_tot_price.setMaximumSize(QSize(16777215, 100))
        self.cust_tot_price.setStyleSheet(u"font: 700 12pt \"SF Pro Display\";")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.cust_tot_price)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_2.addWidget(self.label_17)

        self.txt_cust_date = QLineEdit(self.frame_2)
        self.txt_cust_date.setObjectName(u"txt_cust_date")
        self.txt_cust_date.setMaximumSize(QSize(180, 16777215))
        self.txt_cust_date.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #404040;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.verticalLayout_2.addWidget(self.txt_cust_date)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(350, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 20, -1)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 12pt \"SF Pro Display\";")

        self.verticalLayout_3.addWidget(self.label)

        self.calendarWidget = QCalendarWidget(self.frame_3)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setStyleSheet(u"QCalendarWidget QToolButton {\n"
"    background-color: #ffffff;\n"
"    color: #000000;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    min-width: 0;\n"
"}")

        self.verticalLayout_3.addWidget(self.calendarWidget)

        self.verticalSpacer = QSpacerItem(20, 108, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.frame_19 = QFrame(self.frame_3)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_7 = QSpacerItem(23, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)

        self.btn_clear_2 = QPushButton(self.frame_19)
        self.btn_clear_2.setObjectName(u"btn_clear_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_clear_2.sizePolicy().hasHeightForWidth())
        self.btn_clear_2.setSizePolicy(sizePolicy1)
        self.btn_clear_2.setMinimumSize(QSize(120, 0))
        self.btn_clear_2.setStyleSheet(u"/* Default button style */\n"
"QPushButton {\n"
"    background-color: #C79C99;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #00000;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 8px 16px; \n"
"\n"
"}\n"
"\n"
"/* Button style on hover */\n"
"QPushButton:hover {\n"
" background-color: #46464b;\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"/* Button style when pressed */\n"
"QPushButton:pressed {\n"
"    background-color: #AE544F;\n"
" 	color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: #AE544F;\n"
" 	color: #FFFFFF;\n"
"}")

        self.horizontalLayout_9.addWidget(self.btn_clear_2)

        self.horizontalSpacer_8 = QSpacerItem(2, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)

        self.btn_save_reservation = QPushButton(self.frame_19)
        self.btn_save_reservation.setObjectName(u"btn_save_reservation")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_save_reservation.sizePolicy().hasHeightForWidth())
        self.btn_save_reservation.setSizePolicy(sizePolicy2)
        self.btn_save_reservation.setMinimumSize(QSize(120, 0))
        self.btn_save_reservation.setStyleSheet(u"/* Default button style */\n"
"QPushButton {\n"
"    background-color: #3474D4;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 8px 16px; \n"
"text-align: center;\n"
"\n"
"\n"
"}\n"
"\n"
"/* Button style on hover */\n"
"QPushButton:hover {\n"
" background-color: #A2DCD7;\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"/* Button style when pressed */\n"
"QPushButton:pressed {\n"
"    background-color: #17396D;\n"
" 	color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: #17396D;\n"
" 	color: #FFFFFF;\n"
"}")

        self.horizontalLayout_9.addWidget(self.btn_save_reservation)

        self.horizontalSpacer_9 = QSpacerItem(1, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)


        self.verticalLayout_3.addWidget(self.frame_19)


        self.horizontalLayout.addWidget(self.frame_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        make_reservation_form.setCentralWidget(self.centralwidget)

        self.retranslateUi(make_reservation_form)
        self.btn_clear_2.clicked.connect(self.txt_cust_full_name.clear)
        self.btn_clear_2.clicked.connect(self.txt_cust_email.clear)
        self.btn_clear_2.clicked.connect(self.txt_cust_mobile.clear)
        self.btn_clear_2.clicked.connect(self.cust_no_of_pax.clear)
        self.btn_clear_2.clicked.connect(self.txt_cust_date.clear)

        QMetaObject.connectSlotsByName(make_reservation_form)
    # setupUi

    def retranslateUi(self, make_reservation_form):
        make_reservation_form.setWindowTitle(QCoreApplication.translate("make_reservation_form", u"Make Reservation", None))
        self.label_3.setText(QCoreApplication.translate("make_reservation_form", u"Make Reservation", None))
        self.label_12.setText(QCoreApplication.translate("make_reservation_form", u"Customer_id", None))
        self.txt_cust_id.setPlaceholderText(QCoreApplication.translate("make_reservation_form", u"C001", None))
        self.label_13.setText(QCoreApplication.translate("make_reservation_form", u"Full name", None))
        self.txt_cust_full_name.setPlaceholderText(QCoreApplication.translate("make_reservation_form", u"Enter Your Full Name", None))
        self.label_14.setText(QCoreApplication.translate("make_reservation_form", u"Email", None))
        self.txt_cust_email.setPlaceholderText(QCoreApplication.translate("make_reservation_form", u"Enter Your Email Address", None))
        self.label_15.setText(QCoreApplication.translate("make_reservation_form", u"Mobile", None))
        self.txt_cust_mobile.setPlaceholderText(QCoreApplication.translate("make_reservation_form", u"Enter Your Mobile No.", None))
        self.label_16.setText(QCoreApplication.translate("make_reservation_form", u"No of Pax", None))
        self.cust_tot_price.setText(QCoreApplication.translate("make_reservation_form", u"-- Toal Price --", None))
        self.label_17.setText(QCoreApplication.translate("make_reservation_form", u"Reservation date", None))
        self.txt_cust_date.setPlaceholderText(QCoreApplication.translate("make_reservation_form", u"Select from Calandar", None))
        self.label.setText(QCoreApplication.translate("make_reservation_form", u"Reservation date", None))
        self.btn_clear_2.setText(QCoreApplication.translate("make_reservation_form", u"Clear", None))
        self.btn_save_reservation.setText(QCoreApplication.translate("make_reservation_form", u"Save", None))
    # retranslateUi

