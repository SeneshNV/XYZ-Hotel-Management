# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view_reservationxlaIVq.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import icon_rc

class Ui_view_reservation_form(object):
    def setupUi(self, view_reservation_form):
        if not view_reservation_form.objectName():
            view_reservation_form.setObjectName(u"view_reservation_form")
        view_reservation_form.resize(650, 529)
        view_reservation_form.setMinimumSize(QSize(335, 400))
        view_reservation_form.setStyleSheet(u"border:none;")
        self.horizontalLayout = QHBoxLayout(view_reservation_form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(view_reservation_form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 650, 529))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(100, 40))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.txt_search = QLineEdit(self.frame_4)
        self.txt_search.setObjectName(u"txt_search")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_search.sizePolicy().hasHeightForWidth())
        self.txt_search.setSizePolicy(sizePolicy)
        self.txt_search.setMinimumSize(QSize(300, 0))
        self.txt_search.setStyleSheet(u"QLineEdit{\n"
"    background-color: #D9D9D9;\n"
"	font: 10pt \"SF Pro Display\";\n"
"    color: #000;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px; \n"
"	text-align: left;\n"
"}")
        self.txt_search.setReadOnly(False)

        self.horizontalLayout_3.addWidget(self.txt_search)

        self.btn_search = QPushButton(self.frame_4)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setMinimumSize(QSize(40, 30))
        self.btn_search.setMaximumSize(QSize(40, 30))
        self.btn_search.setStyleSheet(u"/* Default button style */\n"
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
" background-color: #d0d0d0;\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icon/icons8-search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.btn_search)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(40, 30))
        self.pushButton_3.setMaximumSize(QSize(40, 30))
        self.pushButton_3.setStyleSheet(u"/* Default button style */\n"
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
" background-color: #d0d0d0;\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icon/eraser-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.horizontalSpacer_3 = QSpacerItem(236, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.frame_4)

        self.package_list = QScrollArea(self.scrollAreaWidgetContents_2)
        self.package_list.setObjectName(u"package_list")
        self.package_list.setStyleSheet(u"border:none;")
        self.package_list.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 632, 465))
        self.package_list.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.package_list)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout.addWidget(self.scrollArea)


        self.retranslateUi(view_reservation_form)
        self.pushButton_3.clicked.connect(self.txt_search.clear)

        QMetaObject.connectSlotsByName(view_reservation_form)
    # setupUi

    def retranslateUi(self, view_reservation_form):
        view_reservation_form.setWindowTitle(QCoreApplication.translate("view_reservation_form", u"view_package", None))
        self.txt_search.setPlaceholderText(QCoreApplication.translate("view_reservation_form", u"Search Staff", None))
        self.btn_search.setText("")
        self.pushButton_3.setText("")
    # retranslateUi

