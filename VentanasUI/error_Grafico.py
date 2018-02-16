# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error_Grafico.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(293, 167)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 81, 101))
        self.label.setStyleSheet("border-image: url(:/advertencia/220px-Achtung.svg.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(120, 0, 161, 121))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.boton_cerrar = QtWidgets.QPushButton(Dialog)
        self.boton_cerrar.setGeometry(QtCore.QRect(180, 130, 99, 27))
        self.boton_cerrar.setObjectName("boton_cerrar")

        self.retranslateUi(Dialog)
        self.boton_cerrar.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"justify\"><span style=\" color:#ff0000;\">No puede graficar, </span></p><p align=\"justify\"><span style=\" color:#ff0000;\">faltan datos en el  </span></p><p align=\"justify\"><span style=\" color:#ff0000;\">programa!</span></p></body></html>"))
        self.boton_cerrar.setText(_translate("Dialog", "Aceptar"))

import advertencia_rc
