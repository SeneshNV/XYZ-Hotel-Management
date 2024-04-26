# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view_packageddUKpl.ui'
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
from PySide6.QtWidgets import (QApplication, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_view_package_form(object):
    def setupUi(self, view_package_form):
        if not view_package_form.objectName():
            view_package_form.setObjectName(u"view_package_form")
        view_package_form.resize(335, 400)
        view_package_form.setMinimumSize(QSize(335, 400))
        self.verticalLayout = QVBoxLayout(view_package_form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.package_list = QScrollArea(view_package_form)
        self.package_list.setObjectName(u"package_list")
        self.package_list.setStyleSheet(u"border:none;")
        self.package_list.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 317, 382))
        self.package_list.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.package_list)


        self.retranslateUi(view_package_form)

        QMetaObject.connectSlotsByName(view_package_form)
    # setupUi

    def retranslateUi(self, view_package_form):
        view_package_form.setWindowTitle(QCoreApplication.translate("view_package_form", u"view_package", None))
    # retranslateUi

