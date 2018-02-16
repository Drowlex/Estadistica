# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(504, 287)
        Form.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(120, 30, 131, 191))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 91))
        self.label.setStyleSheet("border-image: url(:/about/logo_uv.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(130, 0, 361, 281))
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#0000ff;\">Este proyecto fue realizado</span></p><p align=\"center\"><span style=\" color:#0000ff;\">como proyecto de la Universidad Veracruzana(UV)</span></p><p align=\"center\"><span style=\" color:#0000ff;\">por el estudiante en Ingenieria Informatica</span></p><p align=\"center\"><span style=\" color:#0000ff;\">Pedro Ortiz Luis Roberto </span></p><p align=\"center\"><span style=\" color:#0000ff;\">Acesor: Ing. Gil Arturo Madrid</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:9pt; color:#0000ff;\">Copyright © 2017-2020 UV ESTADISTICA DKL</span></p><p align=\"center\"><span style=\" font-size:9pt; color:#0000ff;\">Version 1.0, Build 0001</span></p></body></html>"))

import about_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

