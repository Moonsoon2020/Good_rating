# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtGui import QColor
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Input(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(650, 500, 131, 61))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 450, 501, 81))
        self.checkBox.setIconSize(QtCore.QSize(20, 20))
        self.checkBox.setAutoRepeatDelay(300)
        self.checkBox.setObjectName("checkBox")
        self.label_login = QtWidgets.QLabel(self.centralwidget)
        self.label_login.setGeometry(QtCore.QRect(30, 260, 55, 16))
        self.label_login.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_login.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_login.setObjectName("label_login")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(30, 390, 55, 16))
        self.label_password.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_password.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_password.setObjectName("label_password")
        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setGeometry(QtCore.QRect(10, 20, 781, 151))
        self.label_info.setAutoFillBackground(False)
        self.label_info.setTextFormat(QtCore.Qt.RichText)
        self.label_info.setScaledContents(False)
        self.label_info.setWordWrap(True)
        self.label_info.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.label_info.setObjectName("label_info")
        self.label_dop_ifo = QtWidgets.QLabel(self.centralwidget)
        self.label_dop_ifo.setGeometry(QtCore.QRect(30, 170, 761, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_dop_ifo.setFont(font)
        self.label_dop_ifo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_dop_ifo.setObjectName("label_dop_ifo")
        self.plainTextEdit_login = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_login.setGeometry(QtCore.QRect(90, 240, 411, 51))
        self.plainTextEdit_login.setObjectName("plainTextEdit_login")
        self.plainTextEdit_password = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_password.setGeometry(QtCore.QRect(90, 370, 411, 51))
        self.plainTextEdit_password.setObjectName("plainTextEdit_password")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Good Rating"))
        self.pushButton.setText(_translate("MainWindow", "Войти"))
        self.checkBox.setText(
            _translate("MainWindow", "Я согласен предоставить свои персональные данные приложению Good Rating. "))
        self.label_login.setText(_translate("MainWindow", "Login"))
        self.label_password.setText(_translate("MainWindow", "Password"))
        self.label_info.setText(_translate("MainWindow",
                                           "<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt; font-weight:600;\">Good Rating </span><span style=\" font-size:12pt;\">- приложение-дополнение для электронного дневника Нижегородской области. Теперь Вам не прийдётся считать: сколько вам нужно получить пятёрок, чтобы в четверти вышла 5, или на какую максимально плохую оценку я могу написать контрольную. </span></p><p align=\"right\"><span style=\" font-size:12pt;\">Приложение работает для </span><span style=\" font-size:12pt; text-decoration: underline;\">всех учеников зарегистрированных на платформе</span><span style=\" font-size:12pt;\">. </span></p></body></html>"))
        self.label_dop_ifo.setText(_translate("MainWindow",
                                              "<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\"> Пожалуйста, введите логин и пароль.</span></p></body></html>"))
        # self.plainTextEdit_login.setPlainText(_translate("MainWindow", "bogdanvoinov9"))
        # self.plainTextEdit_password.setPlainText(_translate("MainWindow", "300905god"))
