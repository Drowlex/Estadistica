# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'talloDeHoja.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1160, 300)
        Form.setStyleSheet("background-color: rgb(170, 85, 0);")
        self.conector = QtWidgets.QPushButton(Form)
        self.conector.setGeometry(QtCore.QRect(1040, 250, 99, 27))
        self.conector.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.conector.setObjectName("conector")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 68, 17))
        self.label_2.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(110, 30, 68, 17))
        self.label_3.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label_3.setObjectName("label_3")
        self.arbol_text = QtWidgets.QTextEdit(Form)
        self.arbol_text.setGeometry(QtCore.QRect(20, 50, 1121, 191))
        self.arbol_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 10px;\n"
"color: rgb(0, 0, 255);")
        self.arbol_text.setObjectName("arbol_text")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(80, 50, 16, 191))
        self.line.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Regresar = QtWidgets.QPushButton(Form)
        self.Regresar.setGeometry(QtCore.QRect(20, 250, 99, 27))
        self.Regresar.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.Regresar.setObjectName("Regresar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Tallo y hoja"))
        self.conector.setText(_translate("Form", "Calcular"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">TALLO</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">HOJA</span></p></body></html>"))
        self.arbol_text.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Century Schoolbook L\'; font-size:12pt; font-weight:56; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  1        [2]</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  2        [3, 4, 5, 6]</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  3        [3, 5, 8, 7]</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  4        [3, 8]</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  5        [9, 1]</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">       Precione &quot;Calcular&quot; para continuar...</p></body></html>"))
        self.Regresar.setText(_translate("Form", "Cerrar"))

