# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view_staffgrHaiS.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)
import icon_rc

class Ui_view_staff_form(object):
    def setupUi(self, view_staff_form):
        if not view_staff_form.objectName():
            view_staff_form.setObjectName(u"view_staff_form")
        view_staff_form.resize(663, 602)
        view_staff_form.setMinimumSize(QSize(335, 400))
        self.horizontalLayout = QHBoxLayout(view_staff_form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.display_mgt_package_2 = QScrollArea(view_staff_form)
        self.display_mgt_package_2.setObjectName(u"display_mgt_package_2")
        self.display_mgt_package_2.setStyleSheet(u"border:none;")
        self.display_mgt_package_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 663, 602))
        self.horizontalLayout_9 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.staff_member_list = QScrollArea(self.scrollAreaWidgetContents_3)
        self.staff_member_list.setObjectName(u"staff_member_list")
        self.staff_member_list.setMinimumSize(QSize(300, 0))
        self.staff_member_list.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 300, 602))
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
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setLineWidth(0)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 363, 602))
        self.scrollAreaWidgetContents_6.setStyleSheet(u"border-radius:10px;")
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.frame_18 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(124, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.staff_member_pp = QLabel(self.frame_18)
        self.staff_member_pp.setObjectName(u"staff_member_pp")
        self.staff_member_pp.setMinimumSize(QSize(120, 120))
        self.staff_member_pp.setStyleSheet(u"background-color: rgb(168, 168, 168);")

        self.horizontalLayout_2.addWidget(self.staff_member_pp)

        self.horizontalSpacer_8 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)

        self.pp_edit = QPushButton(self.frame_18)
        self.pp_edit.setObjectName(u"pp_edit")
        self.pp_edit.setMinimumSize(QSize(24, 24))
        self.pp_edit.setMaximumSize(QSize(24, 24))
        self.pp_edit.setCursor(QCursor(Qt.PointingHandCursor))
        self.pp_edit.setStyleSheet(u"/* Default button style */\n"
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
        icon = QIcon()
        icon.addFile(u":/newPrefix/icon/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pp_edit.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pp_edit)


        self.verticalLayout.addWidget(self.frame_18)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_21 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_21, 0, 0, 1, 1)

        self.view_s_id = QLineEdit(self.scrollAreaWidgetContents_6)
        self.view_s_id.setObjectName(u"view_s_id")
        self.view_s_id.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #404040;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")
        self.view_s_id.setReadOnly(True)

        self.gridLayout.addWidget(self.view_s_id, 0, 1, 1, 1)

        self.label_22 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_22, 1, 0, 1, 1)

        self.view_s_name = QLineEdit(self.scrollAreaWidgetContents_6)
        self.view_s_name.setObjectName(u"view_s_name")
        self.view_s_name.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #404040;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")
        self.view_s_name.setReadOnly(True)
        self.view_s_name.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.view_s_name, 1, 1, 1, 1)

        self.name_edit = QPushButton(self.scrollAreaWidgetContents_6)
        self.name_edit.setObjectName(u"name_edit")
        self.name_edit.setMinimumSize(QSize(24, 24))
        self.name_edit.setMaximumSize(QSize(24, 24))
        self.name_edit.setCursor(QCursor(Qt.PointingHandCursor))
        self.name_edit.setStyleSheet(u"/* Default button style */\n"
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
        self.name_edit.setIcon(icon)

        self.gridLayout.addWidget(self.name_edit, 1, 2, 1, 1)

        self.label_23 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_23, 2, 0, 1, 1)

        self.gender_edit = QPushButton(self.scrollAreaWidgetContents_6)
        self.gender_edit.setObjectName(u"gender_edit")
        self.gender_edit.setMinimumSize(QSize(24, 24))
        self.gender_edit.setMaximumSize(QSize(24, 24))
        self.gender_edit.setCursor(QCursor(Qt.PointingHandCursor))
        self.gender_edit.setStyleSheet(u"/* Default button style */\n"
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
"\n"
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
        self.gender_edit.setIcon(icon)

        self.gridLayout.addWidget(self.gender_edit, 2, 2, 1, 1)

        self.label_20 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_20, 3, 0, 1, 1)

        self.dep_edit = QPushButton(self.scrollAreaWidgetContents_6)
        self.dep_edit.setObjectName(u"dep_edit")
        self.dep_edit.setMinimumSize(QSize(24, 24))
        self.dep_edit.setMaximumSize(QSize(24, 24))
        self.dep_edit.setCursor(QCursor(Qt.PointingHandCursor))
        self.dep_edit.setStyleSheet(u"/* Default button style */\n"
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
"\n"
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
        self.dep_edit.setIcon(icon)

        self.gridLayout.addWidget(self.dep_edit, 3, 2, 1, 1)

        self.label_24 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_24, 4, 0, 1, 1)

        self.view_s_address = QTextEdit(self.scrollAreaWidgetContents_6)
        self.view_s_address.setObjectName(u"view_s_address")
        self.view_s_address.setMaximumSize(QSize(16777215, 80))
        self.view_s_address.setStyleSheet(u"QTextEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #404040;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")
        self.view_s_address.setReadOnly(True)

        self.gridLayout.addWidget(self.view_s_address, 4, 1, 2, 1)

        self.address_edit = QPushButton(self.scrollAreaWidgetContents_6)
        self.address_edit.setObjectName(u"address_edit")
        self.address_edit.setMinimumSize(QSize(24, 24))
        self.address_edit.setMaximumSize(QSize(24, 24))
        self.address_edit.setCursor(QCursor(Qt.PointingHandCursor))
        self.address_edit.setStyleSheet(u"/* Default button style */\n"
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
"\n"
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
        self.address_edit.setIcon(icon)

        self.gridLayout.addWidget(self.address_edit, 5, 2, 1, 1)

        self.label_25 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_25, 6, 0, 1, 1)

        self.view_s_tel = QLineEdit(self.scrollAreaWidgetContents_6)
        self.view_s_tel.setObjectName(u"view_s_tel")
        self.view_s_tel.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #404040;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")
        self.view_s_tel.setReadOnly(True)

        self.gridLayout.addWidget(self.view_s_tel, 6, 1, 1, 1)

        self.tel_edit = QPushButton(self.scrollAreaWidgetContents_6)
        self.tel_edit.setObjectName(u"tel_edit")
        self.tel_edit.setMinimumSize(QSize(24, 24))
        self.tel_edit.setMaximumSize(QSize(24, 24))
        self.tel_edit.setCursor(QCursor(Qt.PointingHandCursor))
        self.tel_edit.setStyleSheet(u"/* Default button style */\n"
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
        self.tel_edit.setIcon(icon)

        self.gridLayout.addWidget(self.tel_edit, 6, 2, 1, 1)

        self.label_26 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_26, 7, 0, 1, 1)

        self.view_s_email = QLineEdit(self.scrollAreaWidgetContents_6)
        self.view_s_email.setObjectName(u"view_s_email")
        self.view_s_email.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #404040;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")
        self.view_s_email.setReadOnly(True)

        self.gridLayout.addWidget(self.view_s_email, 7, 1, 1, 1)

        self.email_edit = QPushButton(self.scrollAreaWidgetContents_6)
        self.email_edit.setObjectName(u"email_edit")
        self.email_edit.setMinimumSize(QSize(24, 24))
        self.email_edit.setMaximumSize(QSize(24, 24))
        self.email_edit.setCursor(QCursor(Qt.PointingHandCursor))
        self.email_edit.setStyleSheet(u"/* Default button style */\n"
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
        self.email_edit.setIcon(icon)

        self.gridLayout.addWidget(self.email_edit, 7, 2, 1, 1)

        self.label_27 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"font: 700 10pt \"SF Pro Display\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_27, 8, 0, 1, 1)

        self.view_s_salary = QLineEdit(self.scrollAreaWidgetContents_6)
        self.view_s_salary.setObjectName(u"view_s_salary")
        self.view_s_salary.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #404040;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")
        self.view_s_salary.setReadOnly(True)

        self.gridLayout.addWidget(self.view_s_salary, 8, 1, 1, 1)

        self.view_s_gender = QComboBox(self.scrollAreaWidgetContents_6)
        self.view_s_gender.addItem("")
        self.view_s_gender.addItem("")
        self.view_s_gender.setObjectName(u"view_s_gender")
        self.view_s_gender.setStyleSheet(u"QComboBox{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #404040;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.gridLayout.addWidget(self.view_s_gender, 2, 1, 1, 1)

        self.view_s_department = QComboBox(self.scrollAreaWidgetContents_6)
        self.view_s_department.addItem("")
        self.view_s_department.addItem("")
        self.view_s_department.addItem("")
        self.view_s_department.addItem("")
        self.view_s_department.setObjectName(u"view_s_department")
        self.view_s_department.setStyleSheet(u"QComboBox{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #404040;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")

        self.gridLayout.addWidget(self.view_s_department, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

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
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view_s_update.sizePolicy().hasHeightForWidth())
        self.view_s_update.setSizePolicy(sizePolicy)
        self.view_s_update.setMinimumSize(QSize(120, 0))
        self.view_s_update.setCursor(QCursor(Qt.PointingHandCursor))
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.view_s_delete.sizePolicy().hasHeightForWidth())
        self.view_s_delete.setSizePolicy(sizePolicy1)
        self.view_s_delete.setMinimumSize(QSize(120, 0))
        self.view_s_delete.setCursor(QCursor(Qt.PointingHandCursor))
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


        self.verticalLayout.addWidget(self.frame_21)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_6)

        self.horizontalLayout_9.addWidget(self.scrollArea_2)

        self.display_mgt_package_2.setWidget(self.scrollAreaWidgetContents_3)

        self.horizontalLayout.addWidget(self.display_mgt_package_2)


        self.retranslateUi(view_staff_form)

        QMetaObject.connectSlotsByName(view_staff_form)
    # setupUi

    def retranslateUi(self, view_staff_form):
        view_staff_form.setWindowTitle(QCoreApplication.translate("view_staff_form", u"view_staff", None))
        self.staff_member_pp.setText("")
#if QT_CONFIG(tooltip)
        self.pp_edit.setToolTip(QCoreApplication.translate("view_staff_form", u"Edit", None))
#endif // QT_CONFIG(tooltip)
        self.pp_edit.setText("")
        self.label_21.setText(QCoreApplication.translate("view_staff_form", u"Staff id", None))
        self.view_s_id.setPlaceholderText(QCoreApplication.translate("view_staff_form", u"S001", None))
        self.label_22.setText(QCoreApplication.translate("view_staff_form", u"Name", None))
        self.view_s_name.setPlaceholderText(QCoreApplication.translate("view_staff_form", u"Staff Member Name", None))
#if QT_CONFIG(tooltip)
        self.name_edit.setToolTip(QCoreApplication.translate("view_staff_form", u"Edit", None))
#endif // QT_CONFIG(tooltip)
        self.name_edit.setText("")
        self.label_23.setText(QCoreApplication.translate("view_staff_form", u"Gander", None))
#if QT_CONFIG(tooltip)
        self.gender_edit.setToolTip(QCoreApplication.translate("view_staff_form", u"Edit", None))
#endif // QT_CONFIG(tooltip)
        self.gender_edit.setText("")
        self.label_20.setText(QCoreApplication.translate("view_staff_form", u"Department", None))
#if QT_CONFIG(tooltip)
        self.dep_edit.setToolTip(QCoreApplication.translate("view_staff_form", u"Edit", None))
#endif // QT_CONFIG(tooltip)
        self.dep_edit.setText("")
        self.label_24.setText(QCoreApplication.translate("view_staff_form", u"Address", None))
        self.view_s_address.setPlaceholderText(QCoreApplication.translate("view_staff_form", u"Staff Member's Address", None))
#if QT_CONFIG(tooltip)
        self.address_edit.setToolTip(QCoreApplication.translate("view_staff_form", u"Edit", None))
#endif // QT_CONFIG(tooltip)
        self.address_edit.setText("")
        self.label_25.setText(QCoreApplication.translate("view_staff_form", u"Tel. Number", None))
        self.view_s_tel.setPlaceholderText(QCoreApplication.translate("view_staff_form", u"07X XX XX XXX", None))
#if QT_CONFIG(tooltip)
        self.tel_edit.setToolTip(QCoreApplication.translate("view_staff_form", u"Edit", None))
#endif // QT_CONFIG(tooltip)
        self.tel_edit.setText("")
        self.label_26.setText(QCoreApplication.translate("view_staff_form", u"E-mail", None))
        self.view_s_email.setPlaceholderText(QCoreApplication.translate("view_staff_form", u"emample : xyz@gmail.com", None))
#if QT_CONFIG(tooltip)
        self.email_edit.setToolTip(QCoreApplication.translate("view_staff_form", u"Edit", None))
#endif // QT_CONFIG(tooltip)
        self.email_edit.setText("")
        self.label_27.setText(QCoreApplication.translate("view_staff_form", u"Salary", None))
        self.view_s_salary.setPlaceholderText(QCoreApplication.translate("view_staff_form", u"Rs. 45000.00", None))
        self.view_s_gender.setItemText(0, QCoreApplication.translate("view_staff_form", u"Male", None))
        self.view_s_gender.setItemText(1, QCoreApplication.translate("view_staff_form", u"Female", None))

        self.view_s_department.setItemText(0, QCoreApplication.translate("view_staff_form", u"Maintenance", None))
        self.view_s_department.setItemText(1, QCoreApplication.translate("view_staff_form", u"Kitchen", None))
        self.view_s_department.setItemText(2, QCoreApplication.translate("view_staff_form", u"Housekeeping", None))
        self.view_s_department.setItemText(3, QCoreApplication.translate("view_staff_form", u"Banquets", None))

        self.view_s_update.setText(QCoreApplication.translate("view_staff_form", u"Update", None))
        self.view_s_delete.setText(QCoreApplication.translate("view_staff_form", u"Delete", None))
    # retranslateUi

