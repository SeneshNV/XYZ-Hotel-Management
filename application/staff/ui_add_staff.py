# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_staffsomSbJ.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_add_staff_form(object):
    def setupUi(self, add_staff_form):
        if not add_staff_form.objectName():
            add_staff_form.setObjectName(u"add_staff_form")
        add_staff_form.resize(618, 566)
        add_staff_form.setMinimumSize(QSize(335, 400))
        add_staff_form.setStyleSheet(u"border:none;")
        self.horizontalLayout = QHBoxLayout(add_staff_form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollArea_3 = QScrollArea(add_staff_form)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setMinimumSize(QSize(200, 0))
        self.scrollArea_3.setStyleSheet(u"")
        self.scrollArea_3.setLineWidth(0)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 698, 531))
        self.horizontalLayout_12 = QHBoxLayout(self.scrollAreaWidgetContents_8)
        self.horizontalLayout_12.setSpacing(20)
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
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy)
        self.frame_25.setMinimumSize(QSize(0, 120))
        self.frame_25.setMaximumSize(QSize(16777215, 100))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, -1)
        self.upload_staff_member_pp_2 = QLabel(self.frame_25)
        self.upload_staff_member_pp_2.setObjectName(u"upload_staff_member_pp_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(50)
        sizePolicy1.setVerticalStretch(50)
        sizePolicy1.setHeightForWidth(self.upload_staff_member_pp_2.sizePolicy().hasHeightForWidth())
        self.upload_staff_member_pp_2.setSizePolicy(sizePolicy1)
        self.upload_staff_member_pp_2.setMinimumSize(QSize(100, 100))
        self.upload_staff_member_pp_2.setMaximumSize(QSize(80, 80))
        self.upload_staff_member_pp_2.setStyleSheet(u"background-color: rgb(168, 168, 168);")

        self.horizontalLayout_14.addWidget(self.upload_staff_member_pp_2)

        self.horizontalSpacer_15 = QSpacerItem(13, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_15)

        self.upload_staff_pp = QPushButton(self.frame_25)
        self.upload_staff_pp.setObjectName(u"upload_staff_pp")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.upload_staff_pp.sizePolicy().hasHeightForWidth())
        self.upload_staff_pp.setSizePolicy(sizePolicy2)
        self.upload_staff_pp.setMinimumSize(QSize(120, 0))
        self.upload_staff_pp.setStyleSheet(u"/* Default button style */\n"
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

        self.horizontalLayout_14.addWidget(self.upload_staff_pp)

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
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.s_upload_g_certificate.sizePolicy().hasHeightForWidth())
        self.s_upload_g_certificate.setSizePolicy(sizePolicy3)
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
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.view_s_upload_g_certificate.sizePolicy().hasHeightForWidth())
        self.view_s_upload_g_certificate.setSizePolicy(sizePolicy4)
        self.view_s_upload_g_certificate.setMinimumSize(QSize(240, 140))
        self.view_s_upload_g_certificate.setMaximumSize(QSize(240, 140))
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
        sizePolicy3.setHeightForWidth(self.s_upload_p_certificate.sizePolicy().hasHeightForWidth())
        self.s_upload_p_certificate.setSizePolicy(sizePolicy3)
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
        sizePolicy4.setHeightForWidth(self.view_s_upload_p_certificate.sizePolicy().hasHeightForWidth())
        self.view_s_upload_p_certificate.setSizePolicy(sizePolicy4)
        self.view_s_upload_p_certificate.setMinimumSize(QSize(240, 140))
        self.view_s_upload_p_certificate.setMaximumSize(QSize(240, 140))
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
        sizePolicy2.setHeightForWidth(self.view_s_update_2.sizePolicy().hasHeightForWidth())
        self.view_s_update_2.setSizePolicy(sizePolicy2)
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

        self.save_insert_data = QPushButton(self.frame_24)
        self.save_insert_data.setObjectName(u"save_insert_data")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.save_insert_data.sizePolicy().hasHeightForWidth())
        self.save_insert_data.setSizePolicy(sizePolicy5)
        self.save_insert_data.setMinimumSize(QSize(120, 0))
        self.save_insert_data.setStyleSheet(u"/* Default button style */\n"
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

        self.horizontalLayout_13.addWidget(self.save_insert_data)

        self.horizontalSpacer_13 = QSpacerItem(1, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_13)


        self.verticalLayout_21.addWidget(self.frame_24)


        self.horizontalLayout_12.addWidget(self.frame_20)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_8)

        self.horizontalLayout.addWidget(self.scrollArea_3)


        self.retranslateUi(add_staff_form)
        self.view_s_update_2.clicked.connect(self.upload_s_name_2.clear)
        self.view_s_update_2.clicked.connect(self.upload_s_address_2.clear)
        self.view_s_update_2.clicked.connect(self.upload_s_tel_2.clear)
        self.view_s_update_2.clicked.connect(self.upload_s_email_2.clear)
        self.view_s_update_2.clicked.connect(self.upload_staff_member_pp_2.clear)
        self.view_s_update_2.clicked.connect(self.view_s_upload_g_certificate.clear)
        self.view_s_update_2.clicked.connect(self.view_s_upload_p_certificate.clear)

        QMetaObject.connectSlotsByName(add_staff_form)
    # setupUi

    def retranslateUi(self, add_staff_form):
        add_staff_form.setWindowTitle(QCoreApplication.translate("add_staff_form", u"Form", None))
        self.label_36.setText(QCoreApplication.translate("add_staff_form", u"Staff Picture", None))
        self.label_28.setText(QCoreApplication.translate("add_staff_form", u"Staff id", None))
        self.upload_s_id_2.setPlaceholderText(QCoreApplication.translate("add_staff_form", u"S001", None))
        self.label_29.setText(QCoreApplication.translate("add_staff_form", u"Name", None))
        self.upload_s_name_2.setPlaceholderText(QCoreApplication.translate("add_staff_form", u"Staff Member Name", None))
        self.label_30.setText(QCoreApplication.translate("add_staff_form", u"Gander", None))
        self.label_31.setText(QCoreApplication.translate("add_staff_form", u"Department", None))
        self.label_32.setText(QCoreApplication.translate("add_staff_form", u"Address", None))
        self.upload_s_address_2.setPlaceholderText(QCoreApplication.translate("add_staff_form", u"Staff Member's Address", None))
        self.label_33.setText(QCoreApplication.translate("add_staff_form", u"Tel. Number", None))
        self.upload_s_tel_2.setPlaceholderText(QCoreApplication.translate("add_staff_form", u"07X XX XX XXX", None))
        self.label_34.setText(QCoreApplication.translate("add_staff_form", u"E-mail", None))
        self.upload_s_email_2.setPlaceholderText(QCoreApplication.translate("add_staff_form", u"emample : xyz@gmail.com", None))
        self.label_35.setText(QCoreApplication.translate("add_staff_form", u"Salary", None))
        self.upload_s_salary_2.setText(QCoreApplication.translate("add_staff_form", u"Rs.45000", None))
        self.upload_s_salary_2.setPlaceholderText(QCoreApplication.translate("add_staff_form", u"Rs. 45000.00", None))
        self.upload_staff_member_pp_2.setText("")
        self.upload_staff_pp.setText(QCoreApplication.translate("add_staff_form", u"Upload Image", None))
        self.upload_s_gender.setItemText(0, QCoreApplication.translate("add_staff_form", u"Male", None))
        self.upload_s_gender.setItemText(1, QCoreApplication.translate("add_staff_form", u"Female", None))

        self.upload_s_department.setItemText(0, QCoreApplication.translate("add_staff_form", u"Maintenance", None))
        self.upload_s_department.setItemText(1, QCoreApplication.translate("add_staff_form", u"Kitchen", None))
        self.upload_s_department.setItemText(2, QCoreApplication.translate("add_staff_form", u"Housekeeping", None))
        self.upload_s_department.setItemText(3, QCoreApplication.translate("add_staff_form", u"Banquets", None))

        self.label_37.setText(QCoreApplication.translate("add_staff_form", u"Grama Niladhari Certificate", None))
        self.s_upload_g_certificate.setText(QCoreApplication.translate("add_staff_form", u"Upload", None))
        self.view_s_upload_g_certificate.setText("")
        self.label_38.setText(QCoreApplication.translate("add_staff_form", u"Police Report", None))
        self.s_upload_p_certificate.setText(QCoreApplication.translate("add_staff_form", u"Upload", None))
        self.view_s_upload_p_certificate.setText("")
        self.view_s_update_2.setText(QCoreApplication.translate("add_staff_form", u"Clear", None))
        self.save_insert_data.setText(QCoreApplication.translate("add_staff_form", u"Save", None))
    # retranslateUi

