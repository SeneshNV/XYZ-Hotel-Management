# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_mainGKIbGE.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTextEdit, QVBoxLayout,
    QWidget)
import icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"font-family: \"SF Pro Display\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setStyleSheet(u"background-color: rgb(174, 84, 79);")
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
        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"font: 700 11pt \"SF Pro Display\";")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_3)

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

        self.verticalLayout.addWidget(self.frame)

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
        self.frame_3.setMinimumSize(QSize(200, 0))
        self.frame_3.setMaximumSize(QSize(200, 16777215))
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
"    background-color: #AE544F;\n"
" 	color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: #AE544F;\n"
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

        self.verticalLayout_7.addWidget(self.btn_dashboard)

        self.btn_mgt_customer = QPushButton(self.frame_12)
        self.btn_mgt_customer.setObjectName(u"btn_mgt_customer")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icon/Report.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_mgt_customer.setIcon(icon1)
        self.btn_mgt_customer.setCheckable(True)

        self.verticalLayout_7.addWidget(self.btn_mgt_customer)

        self.line = QFrame(self.frame_12)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line)

        self.btn_mgt_staff = QPushButton(self.frame_12)
        self.btn_mgt_staff.setObjectName(u"btn_mgt_staff")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icon/Assistant.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/newPrefix/icon/Assistant_W.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_mgt_staff.setIcon(icon2)
        self.btn_mgt_staff.setCheckable(True)

        self.verticalLayout_7.addWidget(self.btn_mgt_staff)

        self.btn_mgt_package = QPushButton(self.frame_12)
        self.btn_mgt_package.setObjectName(u"btn_mgt_package")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/icon/View boards.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/newPrefix/icon/View boards-1.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_mgt_package.setIcon(icon3)
        self.btn_mgt_package.setCheckable(True)

        self.verticalLayout_7.addWidget(self.btn_mgt_package)

        self.line_2 = QFrame(self.frame_12)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_2)

        self.btn_settings = QPushButton(self.frame_12)
        self.btn_settings.setObjectName(u"btn_settings")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/icon/setting_dark.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/newPrefix/icon/setting_light.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_settings.setIcon(icon4)
        self.btn_settings.setIconSize(QSize(11, 11))
        self.btn_settings.setCheckable(True)

        self.verticalLayout_7.addWidget(self.btn_settings)

        self.btn_about_us = QPushButton(self.frame_12)
        self.btn_about_us.setObjectName(u"btn_about_us")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/icon/Feedback.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/newPrefix/icon/Feedback_W.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_about_us.setIcon(icon5)
        self.btn_about_us.setCheckable(True)

        self.verticalLayout_7.addWidget(self.btn_about_us)

        self.line_3 = QFrame(self.frame_12)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_3)

        self.verticalSpacer = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.btn_about_us_2 = QPushButton(self.frame_12)
        self.btn_about_us_2.setObjectName(u"btn_about_us_2")
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/icon/logout-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/newPrefix/icon/logout-svgrepo-com(1).svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_about_us_2.setIcon(icon6)
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
        self.admin_screens = QStackedWidget(self.frame_7)
        self.admin_screens.setObjectName(u"admin_screens")
        self.mgt_package = QWidget()
        self.mgt_package.setObjectName(u"mgt_package")
        self.verticalLayout_11 = QVBoxLayout(self.mgt_package)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_5 = QFrame(self.mgt_package)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 50))
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setStyleSheet(u"#frame_5{\n"
"background: #FFF3F2;\n"
"}\n"
"\n"
"/* Default button style */\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
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
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setLineWidth(0)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_view_package = QPushButton(self.frame_5)
        self.btn_view_package.setObjectName(u"btn_view_package")
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/View boards.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/newPrefix/View boards-1.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_view_package.setIcon(icon7)

        self.horizontalLayout_6.addWidget(self.btn_view_package)

        self.btn_add_package = QPushButton(self.frame_5)
        self.btn_add_package.setObjectName(u"btn_add_package")
        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/Add.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon8.addFile(u":/newPrefix/Add_W.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_add_package.setIcon(icon8)

        self.horizontalLayout_6.addWidget(self.btn_add_package)

        self.horizontalSpacer_2 = QSpacerItem(56, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_11.addWidget(self.frame_5)

        self.admin_mgt_package_screens = QStackedWidget(self.mgt_package)
        self.admin_mgt_package_screens.setObjectName(u"admin_mgt_package_screens")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_12 = QVBoxLayout(self.page_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 12pt \"SF Pro Display\";\n"
"color: rgb(174, 84, 79);")

        self.verticalLayout_12.addWidget(self.label_9)

        self.display_mgt_package = QScrollArea(self.page_3)
        self.display_mgt_package.setObjectName(u"display_mgt_package")
        self.display_mgt_package.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 98, 28))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalSpacer_3 = QSpacerItem(20, 401, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_3)

        self.display_mgt_package.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_12.addWidget(self.display_mgt_package)

        self.admin_mgt_package_screens.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_17 = QVBoxLayout(self.page_4)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_11 = QLabel(self.page_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 12pt \"SF Pro Display\";\n"
"color: rgb(174, 84, 79);")

        self.verticalLayout_17.addWidget(self.label_11)

        self.display_mgt_package_3 = QScrollArea(self.page_4)
        self.display_mgt_package_3.setObjectName(u"display_mgt_package_3")
        self.display_mgt_package_3.setMinimumSize(QSize(0, 424))
        self.display_mgt_package_3.setMaximumSize(QSize(700, 16777215))
        self.display_mgt_package_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 335, 783))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_12 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_12)

        self.txt_p_id = QLineEdit(self.scrollAreaWidgetContents_4)
        self.txt_p_id.setObjectName(u"txt_p_id")
        self.txt_p_id.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.txt_p_id)

        self.label_13 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_13)

        self.txt_p_title = QLineEdit(self.scrollAreaWidgetContents_4)
        self.txt_p_title.setObjectName(u"txt_p_title")
        self.txt_p_title.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.txt_p_title)

        self.label_14 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_14)

        self.txt_p_description = QTextEdit(self.scrollAreaWidgetContents_4)
        self.txt_p_description.setObjectName(u"txt_p_description")
        self.txt_p_description.setStyleSheet(u"QTextEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.txt_p_description)

        self.label_15 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_15)

        self.chk_price = QCheckBox(self.scrollAreaWidgetContents_4)
        self.chk_price.setObjectName(u"chk_price")
        self.chk_price.setStyleSheet(u"QCheckBox{\n"
"    background-color: none;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.chk_price)

        self.label_16 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_16)

        self.cmb_category = QComboBox(self.scrollAreaWidgetContents_4)
        self.cmb_category.setObjectName(u"cmb_category")
        self.cmb_category.setStyleSheet(u"QComboBox{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.cmb_category)

        self.label_17 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_17.setObjectName(u"label_17")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_17)

        self.frame_16 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"QCheckBox{\n"
"    background-color: none;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_16)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.chk_com_wifi = QCheckBox(self.frame_16)
        self.chk_com_wifi.setObjectName(u"chk_com_wifi")

        self.verticalLayout_18.addWidget(self.chk_com_wifi)

        self.chk_com_security = QCheckBox(self.frame_16)
        self.chk_com_security.setObjectName(u"chk_com_security")

        self.verticalLayout_18.addWidget(self.chk_com_security)

        self.chk_com_butler_service = QCheckBox(self.frame_16)
        self.chk_com_butler_service.setObjectName(u"chk_com_butler_service")

        self.verticalLayout_18.addWidget(self.chk_com_butler_service)

        self.chk_com_car = QCheckBox(self.frame_16)
        self.chk_com_car.setObjectName(u"chk_com_car")

        self.verticalLayout_18.addWidget(self.chk_com_car)

        self.chk_com_pool = QCheckBox(self.frame_16)
        self.chk_com_pool.setObjectName(u"chk_com_pool")

        self.verticalLayout_18.addWidget(self.chk_com_pool)

        self.chk_com_24hr_service = QCheckBox(self.frame_16)
        self.chk_com_24hr_service.setObjectName(u"chk_com_24hr_service")

        self.verticalLayout_18.addWidget(self.chk_com_24hr_service)


        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.frame_16)

        self.label_18 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_18.setObjectName(u"label_18")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_18)

        self.lbl_display_img = QLabel(self.scrollAreaWidgetContents_4)
        self.lbl_display_img.setObjectName(u"lbl_display_img")
        self.lbl_display_img.setMinimumSize(QSize(0, 150))
        self.lbl_display_img.setStyleSheet(u"QLabel{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.lbl_display_img)

        self.btn_browser_img = QPushButton(self.scrollAreaWidgetContents_4)
        self.btn_browser_img.setObjectName(u"btn_browser_img")
        self.btn_browser_img.setMaximumSize(QSize(150, 16777215))
        self.btn_browser_img.setStyleSheet(u"/* Default button style */\n"
"QPushButton {\n"
"    background-color: #D9D9D9;\n"
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

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.btn_browser_img)


        self.verticalLayout_16.addLayout(self.formLayout)

        self.frame_17 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_5 = QSpacerItem(23, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.btn_clear = QPushButton(self.frame_17)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setMinimumSize(QSize(120, 0))
        self.btn_clear.setStyleSheet(u"/* Default button style */\n"
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

        self.horizontalLayout_8.addWidget(self.btn_clear)

        self.horizontalSpacer_4 = QSpacerItem(2, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.btn_save_package = QPushButton(self.frame_17)
        self.btn_save_package.setObjectName(u"btn_save_package")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_save_package.sizePolicy().hasHeightForWidth())
        self.btn_save_package.setSizePolicy(sizePolicy1)
        self.btn_save_package.setMinimumSize(QSize(120, 0))
        self.btn_save_package.setStyleSheet(u"/* Default button style */\n"
"QPushButton {\n"
"    background-color: #4C4C6C;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 8px 16px; \n"
"\n"
"\n"
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

        self.horizontalLayout_8.addWidget(self.btn_save_package)

        self.horizontalSpacer_6 = QSpacerItem(1, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)


        self.verticalLayout_16.addWidget(self.frame_17)

        self.display_mgt_package_3.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_17.addWidget(self.display_mgt_package_3)

        self.admin_mgt_package_screens.addWidget(self.page_4)

        self.verticalLayout_11.addWidget(self.admin_mgt_package_screens)

        self.admin_screens.addWidget(self.mgt_package)
        self.add_package = QWidget()
        self.add_package.setObjectName(u"add_package")
        self.verticalLayout_19 = QVBoxLayout(self.add_package)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_15 = QFrame(self.add_package)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 50))
        self.frame_15.setMaximumSize(QSize(16777215, 50))
        self.frame_15.setStyleSheet(u"#frame_5{\n"
"background: #FFF3F2;\n"
"}\n"
"\n"
"/* Default button style */\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
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
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.frame_15.setLineWidth(0)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_view_package_2 = QPushButton(self.frame_15)
        self.btn_view_package_2.setObjectName(u"btn_view_package_2")
        self.btn_view_package_2.setIcon(icon3)

        self.horizontalLayout_7.addWidget(self.btn_view_package_2)

        self.btn_add_package_2 = QPushButton(self.frame_15)
        self.btn_add_package_2.setObjectName(u"btn_add_package_2")
        icon9 = QIcon()
        icon9.addFile(u":/newPrefix/icon/Add.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon9.addFile(u":/newPrefix/icon/Add_W.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_add_package_2.setIcon(icon9)

        self.horizontalLayout_7.addWidget(self.btn_add_package_2)

        self.horizontalSpacer_3 = QSpacerItem(56, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)


        self.verticalLayout_19.addWidget(self.frame_15)

        self.admin_mgt_package_screens_2 = QStackedWidget(self.add_package)
        self.admin_mgt_package_screens_2.setObjectName(u"admin_mgt_package_screens_2")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_14 = QVBoxLayout(self.page_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_10 = QLabel(self.page_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 12pt \"SF Pro Display\";\n"
"color: rgb(174, 84, 79);")

        self.verticalLayout_14.addWidget(self.label_10)

        self.display_mgt_package_2 = QScrollArea(self.page_5)
        self.display_mgt_package_2.setObjectName(u"display_mgt_package_2")
        self.display_mgt_package_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 424, 89))
        self.horizontalLayout_9 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.staff_member_list = QScrollArea(self.scrollAreaWidgetContents_3)
        self.staff_member_list.setObjectName(u"staff_member_list")
        self.staff_member_list.setMinimumSize(QSize(200, 0))
        self.staff_member_list.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 198, 28))
        self.staff_member_list.setWidget(self.scrollAreaWidgetContents_5)

        self.horizontalLayout_9.addWidget(self.staff_member_list)

        self.scrollArea_2 = QScrollArea(self.scrollAreaWidgetContents_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(200, 0))
        self.scrollArea_2.setStyleSheet(u"\n"
"\n"
"\n"
"background-color: rgb(199, 156, 153);\n"
"")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 302, 537))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_18 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_7 = QSpacerItem(124, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.staff_member_pp = QLabel(self.frame_18)
        self.staff_member_pp.setObjectName(u"staff_member_pp")
        self.staff_member_pp.setMinimumSize(QSize(80, 80))
        self.staff_member_pp.setStyleSheet(u"background-color: rgb(168, 168, 168);")

        self.horizontalLayout_10.addWidget(self.staff_member_pp)

        self.horizontalSpacer_8 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)


        self.verticalLayout_15.addWidget(self.frame_18)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_21 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_21)

        self.view_s_id = QLineEdit(self.scrollAreaWidgetContents_6)
        self.view_s_id.setObjectName(u"view_s_id")
        self.view_s_id.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.view_s_id)

        self.label_22 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_22)

        self.view_s_name = QLineEdit(self.scrollAreaWidgetContents_6)
        self.view_s_name.setObjectName(u"view_s_name")
        self.view_s_name.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.view_s_name)

        self.label_23 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_23)

        self.label_20 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_20)

        self.label_24 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_24)

        self.view_s_address = QTextEdit(self.scrollAreaWidgetContents_6)
        self.view_s_address.setObjectName(u"view_s_address")
        self.view_s_address.setMaximumSize(QSize(16777215, 80))
        self.view_s_address.setStyleSheet(u"QTextEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.view_s_address)

        self.label_25 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_25)

        self.view_s_tel = QLineEdit(self.scrollAreaWidgetContents_6)
        self.view_s_tel.setObjectName(u"view_s_tel")
        self.view_s_tel.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.view_s_tel)

        self.label_26 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_26)

        self.view_s_email = QLineEdit(self.scrollAreaWidgetContents_6)
        self.view_s_email.setObjectName(u"view_s_email")
        self.view_s_email.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.view_s_email)

        self.label_27 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_27)

        self.view_s_salary = QLineEdit(self.scrollAreaWidgetContents_6)
        self.view_s_salary.setObjectName(u"view_s_salary")
        self.view_s_salary.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.view_s_salary)

        self.view_s_gender = QLineEdit(self.scrollAreaWidgetContents_6)
        self.view_s_gender.setObjectName(u"view_s_gender")
        self.view_s_gender.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.view_s_gender)

        self.view_s_department = QLineEdit(self.scrollAreaWidgetContents_6)
        self.view_s_department.setObjectName(u"view_s_department")
        self.view_s_department.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.view_s_department)


        self.verticalLayout_15.addLayout(self.formLayout_2)

        self.frame_21 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_9 = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_9)

        self.view_s_update = QPushButton(self.frame_21)
        self.view_s_update.setObjectName(u"view_s_update")
        sizePolicy.setHeightForWidth(self.view_s_update.sizePolicy().hasHeightForWidth())
        self.view_s_update.setSizePolicy(sizePolicy)
        self.view_s_update.setMinimumSize(QSize(120, 0))
        self.view_s_update.setStyleSheet(u"/* Default button style */\n"
"QPushButton {\n"
"    background-color: #D9D9D9;\n"
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

        self.horizontalLayout_11.addWidget(self.view_s_update)

        self.horizontalSpacer_10 = QSpacerItem(31, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_10)

        self.view_s_delete = QPushButton(self.frame_21)
        self.view_s_delete.setObjectName(u"view_s_delete")
        sizePolicy1.setHeightForWidth(self.view_s_delete.sizePolicy().hasHeightForWidth())
        self.view_s_delete.setSizePolicy(sizePolicy1)
        self.view_s_delete.setMinimumSize(QSize(120, 0))
        self.view_s_delete.setStyleSheet(u"/* Default button style */\n"
"QPushButton {\n"
"    background-color: #4C4C6C;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 8px 16px; \n"
"\n"
"\n"
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

        self.horizontalLayout_11.addWidget(self.view_s_delete)

        self.horizontalSpacer_11 = QSpacerItem(32, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)


        self.verticalLayout_15.addWidget(self.frame_21)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_6)

        self.horizontalLayout_9.addWidget(self.scrollArea_2)

        self.display_mgt_package_2.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_14.addWidget(self.display_mgt_package_2)

        self.admin_mgt_package_screens_2.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_20 = QVBoxLayout(self.page_6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_19 = QLabel(self.page_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"font: 12pt \"SF Pro Display\";\n"
"color: rgb(174, 84, 79);")

        self.verticalLayout_20.addWidget(self.label_19)

        self.scrollArea_3 = QScrollArea(self.page_6)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setMinimumSize(QSize(200, 0))
        self.scrollArea_3.setStyleSheet(u"")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 687, 510))
        self.horizontalLayout_12 = QHBoxLayout(self.scrollAreaWidgetContents_8)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_19 = QFrame(self.scrollAreaWidgetContents_8)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_19)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_36 = QLabel(self.frame_19)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: #a8a8a8;")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_36)

        self.label_28 = QLabel(self.frame_19)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: #a8a8a8;")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_28)

        self.upload_s_id_2 = QLineEdit(self.frame_19)
        self.upload_s_id_2.setObjectName(u"upload_s_id_2")
        self.upload_s_id_2.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.upload_s_id_2)

        self.label_29 = QLabel(self.frame_19)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: #a8a8a8;")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_29)

        self.upload_s_name_2 = QLineEdit(self.frame_19)
        self.upload_s_name_2.setObjectName(u"upload_s_name_2")
        self.upload_s_name_2.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.upload_s_name_2)

        self.label_30 = QLabel(self.frame_19)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: #a8a8a8;")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_30)

        self.label_31 = QLabel(self.frame_19)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: #a8a8a8;")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_31)

        self.label_32 = QLabel(self.frame_19)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: #a8a8a8;")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.label_32)

        self.upload_s_address_2 = QTextEdit(self.frame_19)
        self.upload_s_address_2.setObjectName(u"upload_s_address_2")
        self.upload_s_address_2.setMaximumSize(QSize(16777215, 80))
        self.upload_s_address_2.setStyleSheet(u"QTextEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.upload_s_address_2)

        self.label_33 = QLabel(self.frame_19)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: #a8a8a8;")

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.label_33)

        self.upload_s_tel_2 = QLineEdit(self.frame_19)
        self.upload_s_tel_2.setObjectName(u"upload_s_tel_2")
        self.upload_s_tel_2.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.upload_s_tel_2)

        self.label_34 = QLabel(self.frame_19)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: #a8a8a8;")

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.label_34)

        self.upload_s_email_2 = QLineEdit(self.frame_19)
        self.upload_s_email_2.setObjectName(u"upload_s_email_2")
        self.upload_s_email_2.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.upload_s_email_2)

        self.label_35 = QLabel(self.frame_19)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: #a8a8a8;")

        self.formLayout_3.setWidget(8, QFormLayout.LabelRole, self.label_35)

        self.upload_s_salary_2 = QLineEdit(self.frame_19)
        self.upload_s_salary_2.setObjectName(u"upload_s_salary_2")
        self.upload_s_salary_2.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout_3.setWidget(8, QFormLayout.FieldRole, self.upload_s_salary_2)

        self.frame_25 = QFrame(self.frame_19)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy2)
        self.frame_25.setMinimumSize(QSize(0, 120))
        self.frame_25.setMaximumSize(QSize(16777215, 100))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, -1)
        self.upload_staff_member_pp_2 = QLabel(self.frame_25)
        self.upload_staff_member_pp_2.setObjectName(u"upload_staff_member_pp_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(50)
        sizePolicy3.setVerticalStretch(50)
        sizePolicy3.setHeightForWidth(self.upload_staff_member_pp_2.sizePolicy().hasHeightForWidth())
        self.upload_staff_member_pp_2.setSizePolicy(sizePolicy3)
        self.upload_staff_member_pp_2.setMinimumSize(QSize(100, 100))
        self.upload_staff_member_pp_2.setMaximumSize(QSize(80, 80))
        self.upload_staff_member_pp_2.setStyleSheet(u"background-color: rgb(168, 168, 168);")

        self.horizontalLayout_14.addWidget(self.upload_staff_member_pp_2)

        self.horizontalSpacer_15 = QSpacerItem(13, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_15)

        self.view_s_update_5 = QPushButton(self.frame_25)
        self.view_s_update_5.setObjectName(u"view_s_update_5")
        sizePolicy.setHeightForWidth(self.view_s_update_5.sizePolicy().hasHeightForWidth())
        self.view_s_update_5.setSizePolicy(sizePolicy)
        self.view_s_update_5.setMinimumSize(QSize(120, 0))
        self.view_s_update_5.setStyleSheet(u"/* Default button style */\n"
"QPushButton {\n"
"    background-color: #D9D9D9;\n"
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

        self.horizontalLayout_14.addWidget(self.view_s_update_5)

        self.horizontalSpacer_16 = QSpacerItem(17, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_16)


        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.frame_25)

        self.upload_s_gender = QComboBox(self.frame_19)
        self.upload_s_gender.addItem("")
        self.upload_s_gender.addItem("")
        self.upload_s_gender.setObjectName(u"upload_s_gender")
        self.upload_s_gender.setStyleSheet(u"QComboBox{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.upload_s_gender)

        self.upload_s_department = QComboBox(self.frame_19)
        self.upload_s_department.addItem("")
        self.upload_s_department.addItem("")
        self.upload_s_department.addItem("")
        self.upload_s_department.addItem("")
        self.upload_s_department.setObjectName(u"upload_s_department")
        self.upload_s_department.setStyleSheet(u"QComboBox{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.upload_s_department)


        self.verticalLayout_24.addLayout(self.formLayout_3)


        self.horizontalLayout_12.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.scrollAreaWidgetContents_8)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_20)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_22)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_37 = QLabel(self.frame_22)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: #a8a8a8;")

        self.verticalLayout_23.addWidget(self.label_37)

        self.s_upload_g_certificate = QPushButton(self.frame_22)
        self.s_upload_g_certificate.setObjectName(u"s_upload_g_certificate")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.s_upload_g_certificate.sizePolicy().hasHeightForWidth())
        self.s_upload_g_certificate.setSizePolicy(sizePolicy4)
        self.s_upload_g_certificate.setMinimumSize(QSize(120, 0))
        self.s_upload_g_certificate.setStyleSheet(u"/* Default button style */\n"
"QPushButton {\n"
"    background-color: #D9D9D9;\n"
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

        self.verticalLayout_23.addWidget(self.s_upload_g_certificate)

        self.view_s_upload_g_certificate = QLabel(self.frame_22)
        self.view_s_upload_g_certificate.setObjectName(u"view_s_upload_g_certificate")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.view_s_upload_g_certificate.sizePolicy().hasHeightForWidth())
        self.view_s_upload_g_certificate.setSizePolicy(sizePolicy5)
        self.view_s_upload_g_certificate.setMinimumSize(QSize(240, 140))
        self.view_s_upload_g_certificate.setStyleSheet(u"background-color: rgb(168, 168, 168);")

        self.verticalLayout_23.addWidget(self.view_s_upload_g_certificate)


        self.verticalLayout_21.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.frame_20)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_23)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_38 = QLabel(self.frame_23)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: #a8a8a8;")

        self.verticalLayout_22.addWidget(self.label_38)

        self.s_upload_p_certificate = QPushButton(self.frame_23)
        self.s_upload_p_certificate.setObjectName(u"s_upload_p_certificate")
        sizePolicy4.setHeightForWidth(self.s_upload_p_certificate.sizePolicy().hasHeightForWidth())
        self.s_upload_p_certificate.setSizePolicy(sizePolicy4)
        self.s_upload_p_certificate.setMinimumSize(QSize(120, 0))
        self.s_upload_p_certificate.setStyleSheet(u"/* Default button style */\n"
"QPushButton {\n"
"    background-color: #D9D9D9;\n"
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

        self.verticalLayout_22.addWidget(self.s_upload_p_certificate)

        self.view_s_upload_p_certificate = QLabel(self.frame_23)
        self.view_s_upload_p_certificate.setObjectName(u"view_s_upload_p_certificate")
        sizePolicy5.setHeightForWidth(self.view_s_upload_p_certificate.sizePolicy().hasHeightForWidth())
        self.view_s_upload_p_certificate.setSizePolicy(sizePolicy5)
        self.view_s_upload_p_certificate.setMinimumSize(QSize(240, 140))
        self.view_s_upload_p_certificate.setStyleSheet(u"background-color: rgb(168, 168, 168);")

        self.verticalLayout_22.addWidget(self.view_s_upload_p_certificate)


        self.verticalLayout_21.addWidget(self.frame_23)

        self.verticalSpacer_4 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_4)

        self.frame_24 = QFrame(self.frame_20)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 50))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_14 = QSpacerItem(4, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_14)

        self.view_s_update_2 = QPushButton(self.frame_24)
        self.view_s_update_2.setObjectName(u"view_s_update_2")
        sizePolicy.setHeightForWidth(self.view_s_update_2.sizePolicy().hasHeightForWidth())
        self.view_s_update_2.setSizePolicy(sizePolicy)
        self.view_s_update_2.setMinimumSize(QSize(120, 0))
        self.view_s_update_2.setStyleSheet(u"/* Default button style */\n"
"QPushButton {\n"
"    background-color: #D9D9D9;\n"
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

        self.horizontalLayout_13.addWidget(self.view_s_update_2)

        self.horizontalSpacer_12 = QSpacerItem(2, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_12)

        self.view_s_delete_2 = QPushButton(self.frame_24)
        self.view_s_delete_2.setObjectName(u"view_s_delete_2")
        sizePolicy1.setHeightForWidth(self.view_s_delete_2.sizePolicy().hasHeightForWidth())
        self.view_s_delete_2.setSizePolicy(sizePolicy1)
        self.view_s_delete_2.setMinimumSize(QSize(120, 0))
        self.view_s_delete_2.setStyleSheet(u"/* Default button style */\n"
"QPushButton {\n"
"    background-color: #4C4C6C;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 8px 16px; \n"
"\n"
"\n"
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

        self.horizontalLayout_13.addWidget(self.view_s_delete_2)

        self.horizontalSpacer_13 = QSpacerItem(1, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_13)


        self.verticalLayout_21.addWidget(self.frame_24)


        self.horizontalLayout_12.addWidget(self.frame_20)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_8)

        self.verticalLayout_20.addWidget(self.scrollArea_3)

        self.admin_mgt_package_screens_2.addWidget(self.page_6)

        self.verticalLayout_19.addWidget(self.admin_mgt_package_screens_2)

        self.admin_screens.addWidget(self.add_package)

        self.verticalLayout_10.addWidget(self.admin_screens)


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
        self.msg_display_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 178, 487))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_2 = QSpacerItem(20, 466, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)

        self.msg_display_area.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_8.addWidget(self.msg_display_area)


        self.horizontalLayout_2.addWidget(self.frame_8)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_clear.clicked.connect(self.lbl_display_img.clear)
        self.btn_clear.clicked.connect(self.txt_p_title.clear)
        self.btn_clear.clicked.connect(self.txt_p_id.clear)
        self.btn_clear.clicked.connect(self.txt_p_description.clear)
        self.view_s_update_2.clicked.connect(self.upload_s_name_2.clear)
        self.view_s_update_2.clicked.connect(self.upload_s_id_2.clear)
        self.view_s_update_2.clicked.connect(self.upload_staff_member_pp_2.clear)
        self.view_s_update_2.clicked.connect(self.upload_s_address_2.clear)
        self.view_s_update_2.clicked.connect(self.upload_s_tel_2.clear)
        self.view_s_update_2.clicked.connect(self.upload_s_email_2.clear)
        self.view_s_update_2.clicked.connect(self.upload_s_salary_2.clear)
        self.view_s_update_2.clicked.connect(self.view_s_upload_g_certificate.clear)
        self.view_s_update_2.clicked.connect(self.view_s_upload_p_certificate.clear)

        self.admin_screens.setCurrentIndex(1)
        self.admin_mgt_package_screens.setCurrentIndex(1)
        self.admin_mgt_package_screens_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"XYZ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Senesh Nagoda Vithana", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.label.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Hotel Management System", None))
        self.btn_dashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.btn_mgt_customer.setText(QCoreApplication.translate("MainWindow", u"Manage Customers", None))
        self.btn_mgt_staff.setText(QCoreApplication.translate("MainWindow", u"Manage Staff", None))
        self.btn_mgt_package.setText(QCoreApplication.translate("MainWindow", u"Manage Packages", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btn_about_us.setText(QCoreApplication.translate("MainWindow", u"About us", None))
        self.btn_about_us_2.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Developed by :", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Senesh Nagoda Vithana", None))
        self.btn_view_package.setText(QCoreApplication.translate("MainWindow", u"View Packages", None))
        self.btn_add_package.setText(QCoreApplication.translate("MainWindow", u"Add Packages", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Manage Package / View Packages", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Manage Package / Add Packages", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Package id", None))
        self.txt_p_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"P0001", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Package Title", None))
        self.txt_p_title.setPlaceholderText(QCoreApplication.translate("MainWindow", u"example : Outdoor Night Party", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Package Description", None))
        self.txt_p_description.setPlaceholderText(QCoreApplication.translate("MainWindow", u"example : Type about the outdoor Night Party", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Cost per person", None))
        self.chk_price.setText(QCoreApplication.translate("MainWindow", u"Standard Price Method", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Complementary", None))
        self.chk_com_wifi.setText(QCoreApplication.translate("MainWindow", u"FREE WIFI", None))
        self.chk_com_security.setText(QCoreApplication.translate("MainWindow", u"24HR SECURITY", None))
        self.chk_com_butler_service.setText(QCoreApplication.translate("MainWindow", u"BUTLER SERVICE", None))
        self.chk_com_car.setText(QCoreApplication.translate("MainWindow", u"CAR PARKING", None))
        self.chk_com_pool.setText(QCoreApplication.translate("MainWindow", u"INFINITY POOL", None))
        self.chk_com_24hr_service.setText(QCoreApplication.translate("MainWindow", u"24HR SERVICE ", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Package Image", None))
        self.lbl_display_img.setText("")
        self.btn_browser_img.setText(QCoreApplication.translate("MainWindow", u"Browser Image", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.btn_save_package.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_view_package_2.setText(QCoreApplication.translate("MainWindow", u"View Packages", None))
        self.btn_add_package_2.setText(QCoreApplication.translate("MainWindow", u"Add Packages", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Manage Staff / View Staff", None))
        self.staff_member_pp.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Staff id", None))
        self.view_s_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"S001", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.view_s_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Staff Member Name", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Gander", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Department", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.view_s_address.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Staff Member's Address", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Tel. Number", None))
        self.view_s_tel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"07X XX XX XXX", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.view_s_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"emample : xyz@gmail.com", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Salary", None))
        self.view_s_salary.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rs. 45000.00", None))
        self.view_s_gender.setPlaceholderText(QCoreApplication.translate("MainWindow", u"example : Male", None))
        self.view_s_department.setPlaceholderText(QCoreApplication.translate("MainWindow", u"example : Maintenance", None))
        self.view_s_update.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.view_s_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Manage Staff / View Staff", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Staff id", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Staff id", None))
        self.upload_s_id_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"S001", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.upload_s_name_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Staff Member Name", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Gander", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Department", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.upload_s_address_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Staff Member's Address", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Tel. Number", None))
        self.upload_s_tel_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"07X XX XX XXX", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.upload_s_email_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"emample : xyz@gmail.com", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Salary", None))
        self.upload_s_salary_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rs. 45000.00", None))
        self.upload_staff_member_pp_2.setText("")
        self.view_s_update_5.setText(QCoreApplication.translate("MainWindow", u"Upload Image", None))
        self.upload_s_gender.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.upload_s_gender.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))

        self.upload_s_department.setItemText(0, QCoreApplication.translate("MainWindow", u"Maintainence", None))
        self.upload_s_department.setItemText(1, QCoreApplication.translate("MainWindow", u"Kitchen", None))
        self.upload_s_department.setItemText(2, QCoreApplication.translate("MainWindow", u"Housekeeping", None))
        self.upload_s_department.setItemText(3, QCoreApplication.translate("MainWindow", u"Banquets", None))

        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Grama Niladhari Certificate", None))
        self.s_upload_g_certificate.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.view_s_upload_g_certificate.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Police Report", None))
        self.s_upload_p_certificate.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.view_s_upload_p_certificate.setText("")
        self.view_s_update_2.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.view_s_delete_2.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Message", None))
    # retranslateUi

