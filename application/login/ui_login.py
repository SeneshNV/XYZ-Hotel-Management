# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginZUzgIv.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import icon_rc

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(640, 464)
        login.setMaximumSize(QSize(640, 16777215))
        login.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayout = QHBoxLayout(login)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(login)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(310, 338))

        self.horizontalLayout_4.addWidget(self.label_5)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(login)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(330, 16777215))
        self.frame_2.setStyleSheet(u"font-family: 'SF Pro Display';")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(20, -1, -1, -1)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, -1, -1)
        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 12pt \"SF Pro Display\";")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.frame_7)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icon/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/newPrefix/icon/x-circle 2.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame_7)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 700 26pt \"SF Pro Display\";")

        self.verticalLayout.addWidget(self.label_2)


        self.verticalLayout_8.addWidget(self.frame_3)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.txt_u_name = QLineEdit(self.frame_8)
        self.txt_u_name.setObjectName(u"txt_u_name")
        self.txt_u_name.setMinimumSize(QSize(0, 30))
        self.txt_u_name.setStyleSheet(u"border:none;\n"
"background:transparent;\n"
"padding:5px;\n"
"font: 11pt \"SF Pro Display\";")
        self.txt_u_name.setMaxLength(32)

        self.verticalLayout_3.addWidget(self.txt_u_name)

        self.line = QFrame(self.frame_8)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)


        self.verticalLayout_7.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.txt_u_pass = QLineEdit(self.frame_9)
        self.txt_u_pass.setObjectName(u"txt_u_pass")
        self.txt_u_pass.setMinimumSize(QSize(0, 30))
        self.txt_u_pass.setStyleSheet(u"border:none;\n"
"background:transparent;\n"
"padding:5px;\n"
"font: 11pt \"SF Pro Display\";")
        self.txt_u_pass.setMaxLength(10)
        self.txt_u_pass.setEchoMode(QLineEdit.Password)

        self.verticalLayout_5.addWidget(self.txt_u_pass)

        self.line_3 = QFrame(self.frame_9)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_3)


        self.verticalLayout_7.addWidget(self.frame_9)

        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_11)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.cmb_u_acc_type = QComboBox(self.frame_11)
        self.cmb_u_acc_type.addItem("")
        self.cmb_u_acc_type.addItem("")
        self.cmb_u_acc_type.setObjectName(u"cmb_u_acc_type")
        self.cmb_u_acc_type.setMinimumSize(QSize(0, 30))
        self.cmb_u_acc_type.setCursor(QCursor(Qt.PointingHandCursor))
        self.cmb_u_acc_type.setStyleSheet(u"border:none;\n"
"padding: 5px;\n"
"font: 10pt \"SF Pro Display\";\n"
"")

        self.verticalLayout_6.addWidget(self.cmb_u_acc_type)

        self.line_4 = QFrame(self.frame_11)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_4)


        self.verticalLayout_7.addWidget(self.frame_11)


        self.verticalLayout_8.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_login = QPushButton(self.frame_5)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(40, 30))
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(u"background: #AE544F;\n"
"font: 12pt \"SF Pro Display\";\n"
"padding : 8px;\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.btn_login)

        self.btn_forgot_pass = QLabel(self.frame_5)
        self.btn_forgot_pass.setObjectName(u"btn_forgot_pass")
        self.btn_forgot_pass.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btn_forgot_pass)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_create_acc = QLabel(self.frame_6)
        self.btn_create_acc.setObjectName(u"btn_create_acc")
        self.btn_create_acc.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_create_acc.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.btn_create_acc)


        self.verticalLayout_8.addWidget(self.frame_6)


        self.horizontalLayout.addWidget(self.frame_2)


        self.retranslateUi(login)
        self.pushButton.clicked.connect(login.close)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"XYZ - login ", None))
        self.label_5.setText("")
        self.label.setText(QCoreApplication.translate("login", u"Welcome to the XYZ Hotel ", None))
        self.pushButton.setText("")
        self.label_2.setText(QCoreApplication.translate("login", u"Login", None))
        self.txt_u_name.setPlaceholderText(QCoreApplication.translate("login", u"Username", None))
        self.txt_u_pass.setPlaceholderText(QCoreApplication.translate("login", u"Password", None))
        self.cmb_u_acc_type.setItemText(0, QCoreApplication.translate("login", u"User Account", None))
        self.cmb_u_acc_type.setItemText(1, QCoreApplication.translate("login", u"Administrator Account", None))

        self.btn_login.setText(QCoreApplication.translate("login", u"Login", None))
        self.btn_forgot_pass.setText(QCoreApplication.translate("login", u"forgot password ?", None))
        self.btn_create_acc.setText(QCoreApplication.translate("login", u"Create an account", None))
    # retranslateUi

