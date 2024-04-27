# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signupGYafyw.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import icon_rc

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(640, 464)
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
        self.label_5.setMaximumSize(QSize(310, 16777215))

        self.horizontalLayout_4.addWidget(self.label_5)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(login)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(330, 16777215))
        self.frame_2.setStyleSheet(u"font-family: 'SF Pro Display';")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 6, 0, -1)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, -1, 0)
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

        self.horizontalSpacer = QSpacerItem(67, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.frame_7)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icon/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame_7)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 700 26pt \"SF Pro Display\";")

        self.verticalLayout.addWidget(self.label_2)


        self.verticalLayout_8.addWidget(self.frame_3)

        self.verticalSpacer = QSpacerItem(20, 24, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, -1, -1)
        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.txt_nw_uname = QLineEdit(self.frame_8)
        self.txt_nw_uname.setObjectName(u"txt_nw_uname")
        self.txt_nw_uname.setMinimumSize(QSize(0, 30))
        self.txt_nw_uname.setStyleSheet(u"border:none;\n"
"background:transparent;\n"
"padding:5px;\n"
"font: 11pt \"SF Pro Display\";")
        self.txt_nw_uname.setMaxLength(32)

        self.verticalLayout_3.addWidget(self.txt_nw_uname)

        self.line = QFrame(self.frame_8)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)


        self.verticalLayout_7.addWidget(self.frame_8)

        self.frame_12 = QFrame(self.frame_4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_12)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.txt_nw_email = QLineEdit(self.frame_12)
        self.txt_nw_email.setObjectName(u"txt_nw_email")
        self.txt_nw_email.setMinimumSize(QSize(0, 30))
        self.txt_nw_email.setStyleSheet(u"border:none;\n"
"background:transparent;\n"
"padding:5px;\n"
"font: 11pt \"SF Pro Display\";")
        self.txt_nw_email.setMaxLength(50)
        self.txt_nw_email.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_9.addWidget(self.txt_nw_email)

        self.line_5 = QFrame(self.frame_12)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_5)


        self.verticalLayout_7.addWidget(self.frame_12)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.txt_nw_pass = QLineEdit(self.frame_9)
        self.txt_nw_pass.setObjectName(u"txt_nw_pass")
        self.txt_nw_pass.setMinimumSize(QSize(0, 30))
        self.txt_nw_pass.setStyleSheet(u"border:none;\n"
"background:transparent;\n"
"padding:5px;\n"
"font: 11pt \"SF Pro Display\";")
        self.txt_nw_pass.setMaxLength(10)
        self.txt_nw_pass.setEchoMode(QLineEdit.Password)

        self.verticalLayout_5.addWidget(self.txt_nw_pass)

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
        self.txt_nw_re_pass = QLineEdit(self.frame_11)
        self.txt_nw_re_pass.setObjectName(u"txt_nw_re_pass")
        self.txt_nw_re_pass.setMinimumSize(QSize(0, 30))
        self.txt_nw_re_pass.setStyleSheet(u"border:none;\n"
"background:transparent;\n"
"padding:5px;\n"
"font: 11pt \"SF Pro Display\";")
        self.txt_nw_re_pass.setMaxLength(10)
        self.txt_nw_re_pass.setEchoMode(QLineEdit.Password)

        self.verticalLayout_6.addWidget(self.txt_nw_re_pass)

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
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.btn_signup = QPushButton(self.frame_5)
        self.btn_signup.setObjectName(u"btn_signup")
        self.btn_signup.setMinimumSize(QSize(40, 30))
        self.btn_signup.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_signup.setStyleSheet(u"background: #AE544F;\n"
"font: 12pt \"SF Pro Display\";\n"
"padding : 8px;\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.btn_signup)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.verticalSpacer_2 = QSpacerItem(20, 24, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.btn_have_acc = QLabel(self.frame_6)
        self.btn_have_acc.setObjectName(u"btn_have_acc")
        self.btn_have_acc.setMinimumSize(QSize(0, 20))
        self.btn_have_acc.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_have_acc.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.btn_have_acc)


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
        self.label_2.setText(QCoreApplication.translate("login", u"Signup", None))
        self.txt_nw_uname.setPlaceholderText(QCoreApplication.translate("login", u"Username", None))
        self.txt_nw_email.setPlaceholderText(QCoreApplication.translate("login", u"E-mail", None))
        self.txt_nw_pass.setPlaceholderText(QCoreApplication.translate("login", u"Password", None))
        self.txt_nw_re_pass.setPlaceholderText(QCoreApplication.translate("login", u"Password", None))
        self.btn_signup.setText(QCoreApplication.translate("login", u"Sign up", None))
        self.btn_have_acc.setText(QCoreApplication.translate("login", u"I already have an account", None))
    # retranslateUi

