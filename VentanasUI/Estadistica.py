# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Estadistica.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Estadistica(object):
    def setupUi(self, Estadistica):
        Estadistica.setObjectName("Estadistica")
        Estadistica.resize(1029, 703)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/principal/estadistica.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Estadistica.setWindowIcon(icon)
        Estadistica.setStyleSheet("background-color: rgb(0, 127, 93);")
        self.centralwidget = QtWidgets.QWidget(Estadistica)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 31))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label.setObjectName("label")
        self.insertar_text = QtWidgets.QTextEdit(self.centralwidget)
        self.insertar_text.setGeometry(QtCore.QRect(120, 10, 101, 31))
        self.insertar_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.insertar_text.setObjectName("insertar_text")
        self.boton_agregar = QtWidgets.QPushButton(self.centralwidget)
        self.boton_agregar.setGeometry(QtCore.QRect(230, 10, 161, 27))
        self.boton_agregar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_agregar.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.boton_agregar.setObjectName("boton_agregar")
        self.boton_calcular = QtWidgets.QPushButton(self.centralwidget)
        self.boton_calcular.setGeometry(QtCore.QRect(430, 10, 91, 71))
        self.boton_calcular.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_calcular.setMouseTracking(False)
        self.boton_calcular.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.boton_calcular.setObjectName("boton_calcular")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 250, 91, 31))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 300, 91, 31))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label_3.setObjectName("label_3")
        self.moda_text = QtWidgets.QTextEdit(self.centralwidget)
        self.moda_text.setEnabled(True)
        self.moda_text.setGeometry(QtCore.QRect(120, 300, 91, 71))
        self.moda_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.moda_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.moda_text.setObjectName("moda_text")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 250, 131, 31))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 100, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.datos_text = QtWidgets.QTextEdit(self.centralwidget)
        self.datos_text.setEnabled(True)
        self.datos_text.setGeometry(QtCore.QRect(20, 160, 991, 81))
        self.datos_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.datos_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 10px;\n"
"")
        self.datos_text.setObjectName("datos_text")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(230, 300, 131, 31))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 390, 91, 31))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(230, 340, 131, 61))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label_8.setObjectName("label_8")
        self.intervalo1_text = QtWidgets.QTextEdit(self.centralwidget)
        self.intervalo1_text.setEnabled(True)
        self.intervalo1_text.setGeometry(QtCore.QRect(20, 530, 91, 121))
        self.intervalo1_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.intervalo1_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.intervalo1_text.setObjectName("intervalo1_text")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(870, 10, 141, 111))
        self.label_10.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label_10.setStyleSheet("border-image: url(:/logo/logo_uv.jpg);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(360, 420, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.boton_generarE = QtWidgets.QPushButton(self.centralwidget)
        self.boton_generarE.setGeometry(QtCore.QRect(230, 50, 71, 31))
        self.boton_generarE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_generarE.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.boton_generarE.setObjectName("boton_generarE")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(480, 250, 101, 31))
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label_9.setObjectName("label_9")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(480, 300, 101, 31))
        self.label_12.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(480, 350, 101, 31))
        self.label_13.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label_13.setObjectName("label_13")
        self.intervalo2_text = QtWidgets.QTextEdit(self.centralwidget)
        self.intervalo2_text.setEnabled(True)
        self.intervalo2_text.setGeometry(QtCore.QRect(130, 530, 91, 121))
        self.intervalo2_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.intervalo2_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.intervalo2_text.setObjectName("intervalo2_text")
        self.fa_text = QtWidgets.QTextEdit(self.centralwidget)
        self.fa_text.setEnabled(True)
        self.fa_text.setGeometry(QtCore.QRect(240, 530, 91, 121))
        self.fa_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.fa_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.fa_text.setObjectName("fa_text")
        self.faa_text = QtWidgets.QTextEdit(self.centralwidget)
        self.faa_text.setEnabled(True)
        self.faa_text.setGeometry(QtCore.QRect(350, 530, 91, 121))
        self.faa_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.faa_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.faa_text.setObjectName("faa_text")
        self.fr_text = QtWidgets.QTextEdit(self.centralwidget)
        self.fr_text.setEnabled(True)
        self.fr_text.setGeometry(QtCore.QRect(460, 530, 91, 121))
        self.fr_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.fr_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.fr_text.setObjectName("fr_text")
        self.fra_text = QtWidgets.QTextEdit(self.centralwidget)
        self.fra_text.setEnabled(True)
        self.fra_text.setGeometry(QtCore.QRect(570, 530, 91, 121))
        self.fra_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.fra_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.fra_text.setObjectName("fra_text")
        self.ma_text = QtWidgets.QTextEdit(self.centralwidget)
        self.ma_text.setEnabled(True)
        self.ma_text.setGeometry(QtCore.QRect(680, 530, 91, 121))
        self.ma_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.ma_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.ma_text.setObjectName("ma_text")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(20, 470, 91, 51))
        self.label_14.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(130, 470, 91, 51))
        self.label_15.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(240, 470, 91, 51))
        self.label_16.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(350, 470, 91, 51))
        self.label_17.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(460, 470, 91, 51))
        self.label_18.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(570, 470, 91, 51))
        self.label_19.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(680, 470, 91, 51))
        self.label_20.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label_20.setObjectName("label_20")
        self.insertar_random = QtWidgets.QTextEdit(self.centralwidget)
        self.insertar_random.setGeometry(QtCore.QRect(120, 50, 101, 31))
        self.insertar_random.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.insertar_random.setObjectName("insertar_random")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(660, 50, 91, 31))
        self.label_21.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label_21.setObjectName("label_21")
        self.n_datos = QtWidgets.QLabel(self.centralwidget)
        self.n_datos.setGeometry(QtCore.QRect(760, 50, 101, 31))
        self.n_datos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.n_datos.setObjectName("n_datos")
        self.media_text = QtWidgets.QLabel(self.centralwidget)
        self.media_text.setGeometry(QtCore.QRect(120, 250, 91, 31))
        self.media_text.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.media_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.media_text.setText("")
        self.media_text.setObjectName("media_text")
        self.mediana_text = QtWidgets.QLabel(self.centralwidget)
        self.mediana_text.setGeometry(QtCore.QRect(370, 250, 91, 31))
        self.mediana_text.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.mediana_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.mediana_text.setText("")
        self.mediana_text.setObjectName("mediana_text")
        self.intervalos_text = QtWidgets.QLabel(self.centralwidget)
        self.intervalos_text.setGeometry(QtCore.QRect(600, 250, 101, 31))
        self.intervalos_text.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.intervalos_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.intervalos_text.setText("")
        self.intervalos_text.setObjectName("intervalos_text")
        self.rangoM_text = QtWidgets.QLabel(self.centralwidget)
        self.rangoM_text.setGeometry(QtCore.QRect(370, 300, 91, 31))
        self.rangoM_text.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.rangoM_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.rangoM_text.setText("")
        self.rangoM_text.setObjectName("rangoM_text")
        self.rango_text = QtWidgets.QLabel(self.centralwidget)
        self.rango_text.setGeometry(QtCore.QRect(600, 300, 101, 31))
        self.rango_text.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.rango_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.rango_text.setText("")
        self.rango_text.setObjectName("rango_text")
        self.varianza_text = QtWidgets.QLabel(self.centralwidget)
        self.varianza_text.setGeometry(QtCore.QRect(120, 390, 91, 31))
        self.varianza_text.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.varianza_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.varianza_text.setText("")
        self.varianza_text.setObjectName("varianza_text")
        self.desviacion_text = QtWidgets.QLabel(self.centralwidget)
        self.desviacion_text.setGeometry(QtCore.QRect(370, 340, 91, 61))
        self.desviacion_text.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.desviacion_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.desviacion_text.setText("")
        self.desviacion_text.setObjectName("desviacion_text")
        self.amplitud_text = QtWidgets.QLabel(self.centralwidget)
        self.amplitud_text.setGeometry(QtCore.QRect(600, 350, 101, 31))
        self.amplitud_text.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.amplitud_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.amplitud_text.setText("")
        self.amplitud_text.setObjectName("amplitud_text")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(20, 50, 91, 31))
        self.label_22.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label_22.setObjectName("label_22")
        self.boton_graficar = QtWidgets.QPushButton(self.centralwidget)
        self.boton_graficar.setGeometry(QtCore.QRect(900, 480, 111, 111))
        self.boton_graficar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_graficar.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 10px;")
        self.boton_graficar.setObjectName("boton_graficar")
        self.boton_tallo = QtWidgets.QPushButton(self.centralwidget)
        self.boton_tallo.setGeometry(QtCore.QRect(780, 480, 111, 161))
        self.boton_tallo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_tallo.setMouseTracking(False)
        self.boton_tallo.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 10px;")
        self.boton_tallo.setObjectName("boton_tallo")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(710, 350, 101, 61))
        self.label_23.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label_23.setObjectName("label_23")
        self.mediaR_text = QtWidgets.QLabel(self.centralwidget)
        self.mediaR_text.setGeometry(QtCore.QRect(830, 350, 181, 61))
        self.mediaR_text.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.mediaR_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.mediaR_text.setText("")
        self.mediaR_text.setObjectName("mediaR_text")
        self.boton_resetear = QtWidgets.QPushButton(self.centralwidget)
        self.boton_resetear.setGeometry(QtCore.QRect(530, 10, 91, 71))
        self.boton_resetear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_resetear.setMouseTracking(False)
        self.boton_resetear.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.boton_resetear.setObjectName("boton_resetear")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(720, 250, 91, 31))
        self.label_24.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label_24.setObjectName("label_24")
        self.simetria_text = QtWidgets.QLabel(self.centralwidget)
        self.simetria_text.setGeometry(QtCore.QRect(830, 300, 181, 31))
        self.simetria_text.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.simetria_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.simetria_text.setText("")
        self.simetria_text.setObjectName("simetria_text")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(720, 300, 91, 31))
        self.label_25.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label_25.setObjectName("label_25")
        self.curtosis_text = QtWidgets.QLabel(self.centralwidget)
        self.curtosis_text.setGeometry(QtCore.QRect(830, 250, 181, 31))
        self.curtosis_text.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.curtosis_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.curtosis_text.setText("")
        self.curtosis_text.setObjectName("curtosis_text")
        self.boton_salir = QtWidgets.QPushButton(self.centralwidget)
        self.boton_salir.setGeometry(QtCore.QRect(900, 610, 111, 31))
        self.boton_salir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_salir.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.boton_salir.setObjectName("boton_salir")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(650, 10, 101, 31))
        self.label_26.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label_26.setObjectName("label_26")
        self.insertar_porcentaje = QtWidgets.QTextEdit(self.centralwidget)
        self.insertar_porcentaje.setGeometry(QtCore.QRect(120, 90, 101, 31))
        self.insertar_porcentaje.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.insertar_porcentaje.setObjectName("insertar_porcentaje")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(20, 90, 91, 31))
        self.label_27.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.label_27.setObjectName("label_27")
        self.porcentaje_text = QtWidgets.QLabel(self.centralwidget)
        self.porcentaje_text.setGeometry(QtCore.QRect(760, 10, 101, 31))
        self.porcentaje_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.porcentaje_text.setObjectName("porcentaje_text")
        self.boton_porcentaje = QtWidgets.QPushButton(self.centralwidget)
        self.boton_porcentaje.setGeometry(QtCore.QRect(230, 90, 161, 27))
        self.boton_porcentaje.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_porcentaje.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.boton_porcentaje.setObjectName("boton_porcentaje")
        self.boton_generarF = QtWidgets.QPushButton(self.centralwidget)
        self.boton_generarF.setGeometry(QtCore.QRect(310, 50, 81, 31))
        self.boton_generarF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_generarF.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Century Schoolbook L\";\n"
"border-radius: 5px;")
        self.boton_generarF.setObjectName("boton_generarF")
        Estadistica.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Estadistica)
        self.statusbar.setObjectName("statusbar")
        Estadistica.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(Estadistica)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1029, 25))
        self.menubar.setObjectName("menubar")
        Estadistica.setMenuBar(self.menubar)

        self.retranslateUi(Estadistica)
        QtCore.QMetaObject.connectSlotsByName(Estadistica)

    def retranslateUi(self, Estadistica):
        _translate = QtCore.QCoreApplication.translate
        Estadistica.setWindowTitle(_translate("Estadistica", "Estadistica DKL"))
        self.label.setText(_translate("Estadistica", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Valor:</span></p></body></html>"))
        self.insertar_text.setHtml(_translate("Estadistica", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Century Schoolbook L\'; font-size:12pt; font-weight:56; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.boton_agregar.setText(_translate("Estadistica", "Agregar"))
        self.boton_calcular.setText(_translate("Estadistica", "Calcular"))
        self.label_2.setText(_translate("Estadistica", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Media:</span></p></body></html>"))
        self.label_3.setText(_translate("Estadistica", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Moda:</span></p></body></html>"))
        self.label_4.setText(_translate("Estadistica", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Mediana:</span></p></body></html>"))
        self.label_5.setText(_translate("Estadistica", "<html><head/><body><p><span style=\" color:#ffffff;\">Datos Registrados</span></p></body></html>"))
        self.label_6.setText(_translate("Estadistica", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Rango Medio:</span></p></body></html>"))
        self.label_7.setText(_translate("Estadistica", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Varianza:</span></p></body></html>"))
        self.label_8.setText(_translate("Estadistica", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Desviacion </span></p><p align=\"center\"><span style=\" font-size:14pt;\">Estandar:</span></p></body></html>"))
        self.label_11.setText(_translate("Estadistica", "<html><head/><body><p><span style=\" color:#ffffff;\">Tabla de Frecuencias</span></p></body></html>"))
        self.boton_generarE.setText(_translate("Estadistica", "Enteros"))
        self.label_9.setText(_translate("Estadistica", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Intervalos:</span></p></body></html>"))
        self.label_12.setText(_translate("Estadistica", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Rango:</span></p></body></html>"))
        self.label_13.setText(_translate("Estadistica", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Amplitud:</span></p></body></html>"))
        self.label_14.setText(_translate("Estadistica", "<html><head/><body><p align=\"center\">Intervalo </p><p align=\"center\">Menor</p></body></html>"))
        self.label_15.setText(_translate("Estadistica", "<html><head/><body><p align=\"center\">Intervalo </p><p align=\"center\">Mayor</p></body></html>"))
        self.label_16.setText(_translate("Estadistica", "<html><head/><body><p align=\"center\">Frecuencia</p><p align=\"center\">Absoluta</p></body></html>"))
        self.label_17.setText(_translate("Estadistica", "<html><head/><body><p align=\"center\">Frecuencia</p><p align=\"center\">Abs. Acom.</p></body></html>"))
        self.label_18.setText(_translate("Estadistica", "<html><head/><body><p align=\"center\">Frecuencia</p><p align=\"center\">Relativa</p></body></html>"))
        self.label_19.setText(_translate("Estadistica", "<html><head/><body><p align=\"center\">Frecuencia</p><p align=\"center\">Rel. Acom.</p></body></html>"))
        self.label_20.setText(_translate("Estadistica", "<html><head/><body><p align=\"center\">Marca de</p><p align=\"center\">Clase</p></body></html>"))
        self.insertar_random.setHtml(_translate("Estadistica", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Century Schoolbook L\'; font-size:12pt; font-weight:56; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_21.setText(_translate("Estadistica", "<html><head/><body><p align=\"center\">Cantidad:</p></body></html>"))
        self.n_datos.setText(_translate("Estadistica", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_22.setText(_translate("Estadistica", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Generar</span></p></body></html>"))
        self.boton_graficar.setText(_translate("Estadistica", "Graficar"))
        self.boton_tallo.setText(_translate("Estadistica", "Tallo de hoja"))
        self.label_23.setText(_translate("Estadistica", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Media </span></p><p align=\"center\"><span style=\" font-size:14pt;\">Recortada:</span></p></body></html>"))
        self.boton_resetear.setText(_translate("Estadistica", "Reiniciar"))
        self.label_24.setText(_translate("Estadistica", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Curtosis:</span></p></body></html>"))
        self.label_25.setText(_translate("Estadistica", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Simetria:</span></p></body></html>"))
        self.boton_salir.setText(_translate("Estadistica", "Salir"))
        self.label_26.setText(_translate("Estadistica", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Porcentaje:</span></p></body></html>"))
        self.insertar_porcentaje.setHtml(_translate("Estadistica", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Century Schoolbook L\'; font-size:12pt; font-weight:56; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_27.setText(_translate("Estadistica", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">¿%?</span></p></body></html>"))
        self.porcentaje_text.setText(_translate("Estadistica", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.boton_porcentaje.setText(_translate("Estadistica", "%"))
        self.boton_generarF.setText(_translate("Estadistica", "Decimales"))

import logo_principal_rc
import logo_rc
