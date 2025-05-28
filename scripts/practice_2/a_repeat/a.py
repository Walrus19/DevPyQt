# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'a.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(344, 74)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEditInput = QLineEdit(Form)
        self.lineEditInput.setObjectName(u"lineEditInput")

        self.horizontalLayout_2.addWidget(self.lineEditInput)

        self.lineEditMirror = QLineEdit(Form)
        self.lineEditMirror.setObjectName(u"lineEditMirror")

        self.horizontalLayout_2.addWidget(self.lineEditMirror)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonMirror = QPushButton(Form)
        self.pushButtonMirror.setObjectName(u"pushButtonMirror")

        self.horizontalLayout.addWidget(self.pushButtonMirror)

        self.pushButtonClear = QPushButton(Form)
        self.pushButtonClear.setObjectName(u"pushButtonClear")

        self.horizontalLayout.addWidget(self.pushButtonClear)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButtonMirror.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0437\u0432\u0435\u0440\u043d\u0443\u0442\u044c", None))
        self.pushButtonClear.setText(QCoreApplication.translate("Form", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
    # retranslateUi

