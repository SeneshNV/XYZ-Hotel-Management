# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cust_mainAHcOOh.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTextBrowser, QVBoxLayout,
    QWidget)
import icon_rc

class Ui_customer_main_window(object):
    def setupUi(self, customer_main_window):
        if not customer_main_window.objectName():
            customer_main_window.setObjectName(u"customer_main_window")
        customer_main_window.resize(800, 626)
        customer_main_window.setMinimumSize(QSize(800, 600))
        customer_main_window.setStyleSheet(u"font-family: \"SF Pro Display\";")
        self.centralwidget = QWidget(customer_main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_16 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setStyleSheet(u"background-color: #3474D4;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 500 18pt \"ImPerfect23\";\n"
"color: rgb(255, 255, 255);\n"
"margin-left:5px;")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(440, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_9)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 5)
        self.user_name_txt = QLabel(self.frame_9)
        self.user_name_txt.setObjectName(u"user_name_txt")
        self.user_name_txt.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"font: 700 11pt \"SF Pro Display\";")
        self.user_name_txt.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.user_name_txt)

        self.label_2 = QLabel(self.frame_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 11pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_2)


        self.horizontalLayout_4.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_10)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(35, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)


        self.horizontalLayout_4.addWidget(self.frame_10)

        self.frame_9.raise_()
        self.label_4.raise_()
        self.frame_10.raise_()

        self.verticalLayout_16.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(220, 0))
        self.frame_3.setMaximumSize(QSize(220, 16777215))
        self.frame_3.setStyleSheet(u"background: #F2F4FF;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_11 = QFrame(self.frame_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 60))
        self.frame_11.setMaximumSize(QSize(16777215, 60))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.frame_11)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 700 12pt \"SF Pro Display\";")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_5)


        self.verticalLayout_4.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setLayoutDirection(Qt.LeftToRight)
        self.frame_12.setStyleSheet(u"/* Default button style */\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 8px 16px; \n"
"text-align: left;\n"
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
"    background-color: #17396D;\n"
" 	color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: #17396D;\n"
" 	color: #FFFFFF;\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_12)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btn_dashboard = QPushButton(self.frame_12)
        self.btn_dashboard.setObjectName(u"btn_dashboard")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icon/Home.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/newPrefix/icon/Home_W.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_dashboard.setIcon(icon)
        self.btn_dashboard.setCheckable(True)
        self.btn_dashboard.setChecked(True)

        self.verticalLayout_7.addWidget(self.btn_dashboard)

        self.line = QFrame(self.frame_12)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line)

        self.btn_package = QPushButton(self.frame_12)
        self.btn_package.setObjectName(u"btn_package")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icon/logout-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/newPrefix/icon/logout-svgrepo-com(1).svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_package.setIcon(icon1)
        self.btn_package.setCheckable(True)

        self.verticalLayout_7.addWidget(self.btn_package)

        self.btn_view_reser = QPushButton(self.frame_12)
        self.btn_view_reser.setObjectName(u"btn_view_reser")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icon/View boards.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/newPrefix/icon/View boards-1.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_view_reser.setIcon(icon2)
        self.btn_view_reser.setCheckable(True)

        self.verticalLayout_7.addWidget(self.btn_view_reser)

        self.line_2 = QFrame(self.frame_12)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_2)

        self.verticalSpacer = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.btn_about_us_2 = QPushButton(self.frame_12)
        self.btn_about_us_2.setObjectName(u"btn_about_us_2")
        self.btn_about_us_2.setIcon(icon1)
        self.btn_about_us_2.setCheckable(True)

        self.verticalLayout_7.addWidget(self.btn_about_us_2)


        self.verticalLayout_4.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 60))
        self.frame_13.setMaximumSize(QSize(16777215, 60))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_13)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.frame_13)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 10pt \"SF Pro Display\";")

        self.verticalLayout_6.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_13)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";")

        self.verticalLayout_6.addWidget(self.label_7)


        self.verticalLayout_4.addWidget(self.frame_13)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_7.setLineWidth(0)
        self.verticalLayout_10 = QVBoxLayout(self.frame_7)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.cust_screens = QStackedWidget(self.frame_7)
        self.cust_screens.setObjectName(u"cust_screens")
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.horizontalLayout_8 = QHBoxLayout(self.dashboard)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_20 = QFrame(self.dashboard)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_20)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_12 = QLabel(self.frame_20)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font: 500 18pt \"ImPerfect23\";\n"
"color: rgb(52, 116, 212);\n"
"margin-left:5px;")

        self.verticalLayout_13.addWidget(self.label_12)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_13.addItem(self.verticalSpacer_3)

        self.textBrowser = QTextBrowser(self.frame_20)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"border:none;")

        self.verticalLayout_13.addWidget(self.textBrowser)


        self.horizontalLayout_8.addWidget(self.frame_20)

        self.cust_screens.addWidget(self.dashboard)
        self.mgt_package = QWidget()
        self.mgt_package.setObjectName(u"mgt_package")
        self.verticalLayout_11 = QVBoxLayout(self.mgt_package)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.mgt_package)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 50))
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setStyleSheet(u"#frame_5{\n"
"background: #C7FFF9;\n"
"}\n"
"\n"
"/* Default button style */\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #3474D4;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 8px 16px; \n"
"text-align: left;\n"
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
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setLineWidth(0)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_view_package = QPushButton(self.frame_5)
        self.btn_view_package.setObjectName(u"btn_view_package")
        self.btn_view_package.setIcon(icon2)
        self.btn_view_package.setCheckable(True)
        self.btn_view_package.setChecked(True)

        self.horizontalLayout_6.addWidget(self.btn_view_package)

        self.horizontalSpacer_2 = QSpacerItem(56, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_11.addWidget(self.frame_5)

        self.package_screens = QStackedWidget(self.mgt_package)
        self.package_screens.setObjectName(u"package_screens")
        self.view_package = QWidget()
        self.view_package.setObjectName(u"view_package")
        self.verticalLayout_12 = QVBoxLayout(self.view_package)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, -1, -1, 0)
        self.label_9 = QLabel(self.view_package)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 20))
        self.label_9.setMaximumSize(QSize(16777215, 20))
        self.label_9.setStyleSheet(u"font: 12pt \"SF Pro Display\";\n"
"color: #17396D;")

        self.verticalLayout_12.addWidget(self.label_9)

        self.frame_17 = QFrame(self.view_package)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_17)

        self.package_screens.addWidget(self.view_package)
        self.mgt_reservation = QWidget()
        self.mgt_reservation.setObjectName(u"mgt_reservation")
        self.verticalLayout_15 = QVBoxLayout(self.mgt_reservation)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(9, -1, -1, 0)
        self.label_11 = QLabel(self.mgt_reservation)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 20))
        self.label_11.setMaximumSize(QSize(16777215, 20))
        self.label_11.setStyleSheet(u"font: 12pt \"SF Pro Display\";\n"
"color: rgb(174, 84, 79);")

        self.verticalLayout_15.addWidget(self.label_11)

        self.frame_16 = QFrame(self.mgt_reservation)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.frame_16.setLineWidth(0)

        self.verticalLayout_15.addWidget(self.frame_16)

        self.package_screens.addWidget(self.mgt_reservation)

        self.verticalLayout_11.addWidget(self.package_screens)

        self.cust_screens.addWidget(self.mgt_package)
        self.mgt_reservation_2 = QWidget()
        self.mgt_reservation_2.setObjectName(u"mgt_reservation_2")
        self.verticalLayout_19 = QVBoxLayout(self.mgt_reservation_2)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.mgt_reservation_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 50))
        self.frame_15.setMaximumSize(QSize(16777215, 50))
        self.frame_15.setStyleSheet(u"#frame_15{\n"
"background: #C7FFF9;\n"
"}\n"
"\n"
"/* Default button style */\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #3474D4;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 8px 16px; \n"
"text-align: left;\n"
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
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.frame_15.setLineWidth(0)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_view_reservations = QPushButton(self.frame_15)
        self.btn_view_reservations.setObjectName(u"btn_view_reservations")
        self.btn_view_reservations.setIcon(icon2)
        self.btn_view_reservations.setCheckable(True)
        self.btn_view_reservations.setChecked(True)

        self.horizontalLayout_7.addWidget(self.btn_view_reservations)

        self.horizontalSpacer_3 = QSpacerItem(56, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)


        self.verticalLayout_19.addWidget(self.frame_15)

        self.reservation_screens_2 = QStackedWidget(self.mgt_reservation_2)
        self.reservation_screens_2.setObjectName(u"reservation_screens_2")
        self.view_staff = QWidget()
        self.view_staff.setObjectName(u"view_staff")
        self.verticalLayout_14 = QVBoxLayout(self.view_staff)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, -1, -1, 0)
        self.label_10 = QLabel(self.view_staff)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 20))
        self.label_10.setMaximumSize(QSize(16777215, 20))
        self.label_10.setStyleSheet(u"font: 12pt \"SF Pro Display\";\n"
"color:rgb(23, 57, 109);")

        self.verticalLayout_14.addWidget(self.label_10)

        self.frame_18 = QFrame(self.view_staff)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.frame_18)

        self.reservation_screens_2.addWidget(self.view_staff)
        self.add_staff = QWidget()
        self.add_staff.setObjectName(u"add_staff")
        self.verticalLayout = QVBoxLayout(self.add_staff)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.label_19 = QLabel(self.add_staff)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 20))
        self.label_19.setMaximumSize(QSize(16777215, 20))
        self.label_19.setStyleSheet(u"font: 12pt \"SF Pro Display\";\n"
"color: rgb(174, 84, 79);")

        self.verticalLayout.addWidget(self.label_19)

        self.frame_19 = QFrame(self.add_staff)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_19)

        self.reservation_screens_2.addWidget(self.add_staff)

        self.verticalLayout_19.addWidget(self.reservation_screens_2)

        self.cust_screens.addWidget(self.mgt_reservation_2)

        self.verticalLayout_10.addWidget(self.cust_screens)


        self.horizontalLayout_2.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(200, 0))
        self.frame_8.setMaximumSize(QSize(200, 16777215))
        self.frame_8.setStyleSheet(u"background: #F2F4FF;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_8.setLineWidth(0)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.frame_14 = QFrame(self.frame_8)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 30))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.frame_14)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 700 11pt \"SF Pro Display\";")

        self.horizontalLayout_5.addWidget(self.label_8)


        self.verticalLayout_8.addWidget(self.frame_14)

        self.msg_display_area = QScrollArea(self.frame_8)
        self.msg_display_area.setObjectName(u"msg_display_area")
        self.msg_display_area.setStyleSheet(u"border:none;")
        self.msg_display_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 180, 515))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_2 = QSpacerItem(20, 466, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)

        self.msg_display_area.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_8.addWidget(self.msg_display_area)


        self.horizontalLayout_2.addWidget(self.frame_8)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout_16.addWidget(self.frame_2)

        customer_main_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(customer_main_window)

        self.cust_screens.setCurrentIndex(0)
        self.package_screens.setCurrentIndex(0)
        self.reservation_screens_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(customer_main_window)
    # setupUi

    def retranslateUi(self, customer_main_window):
        customer_main_window.setWindowTitle(QCoreApplication.translate("customer_main_window", u"XYZ - Customer Application", None))
        self.label_4.setText(QCoreApplication.translate("customer_main_window", u"Hotel XYZ", None))
        self.user_name_txt.setText(QCoreApplication.translate("customer_main_window", u"Senesh Nagoda Vithana", None))
        self.label_2.setText(QCoreApplication.translate("customer_main_window", u"Customer", None))
        self.label.setText("")
        self.label_5.setText(QCoreApplication.translate("customer_main_window", u"Hotel Management System", None))
        self.btn_dashboard.setText(QCoreApplication.translate("customer_main_window", u"Dashboard", None))
        self.btn_package.setText(QCoreApplication.translate("customer_main_window", u"Packages", None))
        self.btn_view_reser.setText(QCoreApplication.translate("customer_main_window", u"View Reservation", None))
        self.btn_about_us_2.setText(QCoreApplication.translate("customer_main_window", u"Logout", None))
        self.label_6.setText(QCoreApplication.translate("customer_main_window", u"Developed by :", None))
        self.label_7.setText(QCoreApplication.translate("customer_main_window", u"Senesh Nagoda Vithana", None))
        self.label_12.setText(QCoreApplication.translate("customer_main_window", u"Hotel XYZ", None))
        self.textBrowser.setHtml(QCoreApplication.translate("customer_main_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SF Pro Display'; font-size:9pt;\">Here's a concise summary:</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-family:'SF Pro Display'; font-size:9pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span"
                        " style=\" font-weight:700;\">Authentication and Authorization:</span>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" font-family:'SF Pro Display'; font-size:9pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Users log in with username and password.</li>\n"
"<li style=\" font-family:'SF Pro Display'; font-size:9pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Customer accounts supported.</li></ul></li>\n"
"<li style=\" font-family:'SF Pro Display'; font-size:9pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Main Menu:</span>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" font-family:'SF Pro Di"
                        "splay'; font-size:9pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Manage Reservations.</li>\n"
"<li style=\" font-family:'SF Pro Display'; font-size:9pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">View Packages.</li></ul></li>\n"
"<li style=\" font-family:'SF Pro Display'; font-size:9pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Manage Reservations:</span>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" font-family:'SF Pro Display'; font-size:9pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter reservation details.</li>\n"
"<li style=\" font-family:'SF Pro Display'; font-size:9pt;\" style=\""
                        " margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Calculate total cost based on pax.</li>\n"
"<li style=\" font-family:'SF Pro Display'; font-size:9pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Buttons: Create, Edit, Cancel.</li></ul></li>\n"
"<li style=\" font-family:'SF Pro Display'; font-size:9pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">View Packages:</span>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" font-family:'SF Pro Display'; font-size:9pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Search packages by name.</li>\n"
"<li style=\" font-family:'SF Pro Display'; font-size:9pt;\" style=\" margin-to"
                        "p:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Display package details.</li></ul></li></ol></body></html>", None))
        self.btn_view_package.setText(QCoreApplication.translate("customer_main_window", u"View Packages", None))
        self.label_9.setText(QCoreApplication.translate("customer_main_window", u"Package / View Packages", None))
        self.label_11.setText(QCoreApplication.translate("customer_main_window", u"Package / Manage Reservations", None))
        self.btn_view_reservations.setText(QCoreApplication.translate("customer_main_window", u"View Reservation", None))
        self.label_10.setText(QCoreApplication.translate("customer_main_window", u"View Reservation", None))
        self.label_19.setText(QCoreApplication.translate("customer_main_window", u"Manage Staff / Add Staff", None))
        self.label_8.setText(QCoreApplication.translate("customer_main_window", u"Message", None))
    # retranslateUi

