# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'update_packageKdTqsh.ui'
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
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_update_package(object):
    def setupUi(self, update_package):
        if not update_package.objectName():
            update_package.setObjectName(u"update_package")
        update_package.resize(800, 600)
        self.centralwidget = QWidget(update_package)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.display_mgt_package_3 = QScrollArea(self.centralwidget)
        self.display_mgt_package_3.setObjectName(u"display_mgt_package_3")
        self.display_mgt_package_3.setMinimumSize(QSize(200, 0))
        self.display_mgt_package_3.setMaximumSize(QSize(16777215, 16777215))
        self.display_mgt_package_3.setStyleSheet(u"border:none;")
        self.display_mgt_package_3.setLineWidth(0)
        self.display_mgt_package_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 782, 582))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.scrollAreaWidgetContents_4)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_12)

        self.txt_p_id = QLineEdit(self.frame)
        self.txt_p_id.setObjectName(u"txt_p_id")
        self.txt_p_id.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #404040;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.txt_p_id)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_13)

        self.txt_p_title = QLineEdit(self.frame)
        self.txt_p_title.setObjectName(u"txt_p_title")
        self.txt_p_title.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #404040;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.txt_p_title)

        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_14)

        self.txt_p_description = QTextEdit(self.frame)
        self.txt_p_description.setObjectName(u"txt_p_description")
        self.txt_p_description.setStyleSheet(u"QTextEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #404040;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.txt_p_description)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_15)

        self.chk_price = QCheckBox(self.frame)
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

        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_16)

        self.cmb_category = QComboBox(self.frame)
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

        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_17)

        self.frame_16 = QFrame(self.frame)
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


        self.verticalLayout.addLayout(self.formLayout)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_25 = QLabel(self.frame_2)
        self.label_25.setObjectName(u"label_25")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_25)

        self.btn_browser_img_2 = QPushButton(self.frame_2)
        self.btn_browser_img_2.setObjectName(u"btn_browser_img_2")
        self.btn_browser_img_2.setMaximumSize(QSize(150, 16777215))
        self.btn_browser_img_2.setStyleSheet(u"/* Default button style */\n"
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

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.btn_browser_img_2)

        self.lbl_display_img_2 = QLabel(self.frame_2)
        self.lbl_display_img_2.setObjectName(u"lbl_display_img_2")
        self.lbl_display_img_2.setMinimumSize(QSize(0, 160))
        self.lbl_display_img_2.setMaximumSize(QSize(240, 160))
        self.lbl_display_img_2.setStyleSheet(u"QLabel{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #4C4C6C;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lbl_display_img_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(2, QFormLayout.FieldRole, self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.formLayout_2)

        self.frame_19 = QFrame(self.frame_2)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_7 = QSpacerItem(23, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)

        self.btn_clear_2 = QPushButton(self.frame_19)
        self.btn_clear_2.setObjectName(u"btn_clear_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear_2.sizePolicy().hasHeightForWidth())
        self.btn_clear_2.setSizePolicy(sizePolicy)
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

        self.btn_save_package_2 = QPushButton(self.frame_19)
        self.btn_save_package_2.setObjectName(u"btn_save_package_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_save_package_2.sizePolicy().hasHeightForWidth())
        self.btn_save_package_2.setSizePolicy(sizePolicy1)
        self.btn_save_package_2.setMinimumSize(QSize(120, 0))
        self.btn_save_package_2.setStyleSheet(u"/* Default button style */\n"
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

        self.horizontalLayout_9.addWidget(self.btn_save_package_2)

        self.horizontalSpacer_9 = QSpacerItem(1, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)


        self.verticalLayout_2.addWidget(self.frame_19)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.display_mgt_package_3.setWidget(self.scrollAreaWidgetContents_4)

        self.horizontalLayout.addWidget(self.display_mgt_package_3)

        update_package.setCentralWidget(self.centralwidget)

        self.retranslateUi(update_package)

        QMetaObject.connectSlotsByName(update_package)
    # setupUi

    def retranslateUi(self, update_package):
        update_package.setWindowTitle(QCoreApplication.translate("update_package", u"Update Package", None))
        self.label_12.setText(QCoreApplication.translate("update_package", u"Package id", None))
        self.txt_p_id.setPlaceholderText(QCoreApplication.translate("update_package", u"P0001", None))
        self.label_13.setText(QCoreApplication.translate("update_package", u"Package Title", None))
        self.txt_p_title.setPlaceholderText(QCoreApplication.translate("update_package", u"example : Outdoor Night Party", None))
        self.label_14.setText(QCoreApplication.translate("update_package", u"Package Description", None))
        self.txt_p_description.setPlaceholderText(QCoreApplication.translate("update_package", u"example : Type about the outdoor Night Party", None))
        self.label_15.setText(QCoreApplication.translate("update_package", u"Cost per person", None))
        self.chk_price.setText(QCoreApplication.translate("update_package", u"Standard Price Method", None))
        self.label_16.setText(QCoreApplication.translate("update_package", u"Category", None))
        self.label_17.setText(QCoreApplication.translate("update_package", u"Complementary", None))
        self.chk_com_wifi.setText(QCoreApplication.translate("update_package", u"FREE WIFI", None))
        self.chk_com_security.setText(QCoreApplication.translate("update_package", u"24HR SECURITY", None))
        self.chk_com_butler_service.setText(QCoreApplication.translate("update_package", u"BUTLER SERVICE", None))
        self.chk_com_car.setText(QCoreApplication.translate("update_package", u"CAR PARKING", None))
        self.chk_com_pool.setText(QCoreApplication.translate("update_package", u"INFINITY POOL", None))
        self.chk_com_24hr_service.setText(QCoreApplication.translate("update_package", u"24HR SERVICE ", None))
        self.label_25.setText(QCoreApplication.translate("update_package", u"Package Image", None))
        self.btn_browser_img_2.setText(QCoreApplication.translate("update_package", u"Browser Image", None))
        self.lbl_display_img_2.setText("")
        self.btn_clear_2.setText(QCoreApplication.translate("update_package", u"Clear", None))
        self.btn_save_package_2.setText(QCoreApplication.translate("update_package", u"Save", None))
    # retranslateUi

