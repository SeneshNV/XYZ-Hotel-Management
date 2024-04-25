# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_packagehpiYWv.ui'
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
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_add_package_form(object):
    def setupUi(self, add_package_form):
        if not add_package_form.objectName():
            add_package_form.setObjectName(u"add_package_form")
        add_package_form.resize(335, 400)
        add_package_form.setMinimumSize(QSize(335, 400))
        self.horizontalLayout = QHBoxLayout(add_package_form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.display_mgt_package_3 = QScrollArea(add_package_form)
        self.display_mgt_package_3.setObjectName(u"display_mgt_package_3")
        self.display_mgt_package_3.setMinimumSize(QSize(0, 424))
        self.display_mgt_package_3.setMaximumSize(QSize(700, 16777215))
        self.display_mgt_package_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 324, 783))
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

        self.horizontalLayout.addWidget(self.display_mgt_package_3)


        self.retranslateUi(add_package_form)

        QMetaObject.connectSlotsByName(add_package_form)
    # setupUi

    def retranslateUi(self, add_package_form):
        add_package_form.setWindowTitle(QCoreApplication.translate("add_package_form", u"add_package", None))
        self.label_12.setText(QCoreApplication.translate("add_package_form", u"Package id", None))
        self.txt_p_id.setPlaceholderText(QCoreApplication.translate("add_package_form", u"P0001", None))
        self.label_13.setText(QCoreApplication.translate("add_package_form", u"Package Title", None))
        self.txt_p_title.setPlaceholderText(QCoreApplication.translate("add_package_form", u"example : Outdoor Night Party", None))
        self.label_14.setText(QCoreApplication.translate("add_package_form", u"Package Description", None))
        self.txt_p_description.setPlaceholderText(QCoreApplication.translate("add_package_form", u"example : Type about the outdoor Night Party", None))
        self.label_15.setText(QCoreApplication.translate("add_package_form", u"Cost per person", None))
        self.chk_price.setText(QCoreApplication.translate("add_package_form", u"Standard Price Method", None))
        self.label_16.setText(QCoreApplication.translate("add_package_form", u"Category", None))
        self.label_17.setText(QCoreApplication.translate("add_package_form", u"Complementary", None))
        self.chk_com_wifi.setText(QCoreApplication.translate("add_package_form", u"FREE WIFI", None))
        self.chk_com_security.setText(QCoreApplication.translate("add_package_form", u"24HR SECURITY", None))
        self.chk_com_butler_service.setText(QCoreApplication.translate("add_package_form", u"BUTLER SERVICE", None))
        self.chk_com_car.setText(QCoreApplication.translate("add_package_form", u"CAR PARKING", None))
        self.chk_com_pool.setText(QCoreApplication.translate("add_package_form", u"INFINITY POOL", None))
        self.chk_com_24hr_service.setText(QCoreApplication.translate("add_package_form", u"24HR SERVICE ", None))
        self.label_18.setText(QCoreApplication.translate("add_package_form", u"Package Image", None))
        self.lbl_display_img.setText("")
        self.btn_browser_img.setText(QCoreApplication.translate("add_package_form", u"Browser Image", None))
        self.btn_clear.setText(QCoreApplication.translate("add_package_form", u"Clear", None))
        self.btn_save_package.setText(QCoreApplication.translate("add_package_form", u"Save", None))
    # retranslateUi

