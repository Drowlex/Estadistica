# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(256, 117)
        Form.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(100, 9, 151, 31))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.textEdit.setObjectName("textEdit")
        self.Ingresar = QtWidgets.QPushButton(Form)
        self.Ingresar.setGeometry(QtCore.QRect(160, 91, 78, 21))
        self.Ingresar.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.Ingresar.setObjectName("Ingresar")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(11, 50, 77, 21))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(100, 50, 151, 31))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.salir = QtWidgets.QPushButton(Form)
        self.salir.setGeometry(QtCore.QRect(70, 90, 78, 21))
        self.salir.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.salir.setObjectName("salir")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ingreso"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\">User:</p></body></html>"))
        self.Ingresar.setText(_translate("Form", "Ingresar"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\">Password:</p></body></html>"))
        self.salir.setText(_translate("Form", "Salir"))

