#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Librerias del sistema y librerias necesarias para el manejo de Pyqt
import sys
from PyQt5.QtWidgets import QDialog, QPushButton, QLabel
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QIcon
#Imagenes 
from logos import about_rc, advertencia_rc, advertencia2_rc
#Redireccionamiento a sitio web
import webbrowser
#Librerias utilizadas para realizar las operaciones
from formulas import calculos, porcentajes, tallo
#Uso de dialogos
from dialogos import dialogo1, dialogo2, acercade
#Uso de funciones el restablecimiento de los registros
from limpieza import limpiador
#Encargado de llenar los registros
from registrador import add, randomEnteros, randomFlotantes
#Utilizado para graficar los datos registrados
from graficador import graficadora
#PushButton
from utiles import botones, menu_bar
qtCreatorFile = "VentanasUI/Estadistica.ui" # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class AppEstadistica(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,inicio):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #*****************CREADOR DE BOTONES*******************
        botones.botonera(self)
        #****************CREADOR DE MENU BAR*******************
        menu_bar.menuB(self)
        #********************VARIABLES*************************
        self.lista = []
        self.n = inicio
        self.porciento = inicio
        self.maximo = inicio
        self.absoluta = inicio
        self.intervalos = inicio
        self.rango = inicio
        self.amplitud = inicio
        self.tabla = {}
        #*******************FUNCION IMPRIMIR*******************
    def talloDeHoja(self):#Llamo a un widget
        try:
            if self.n != 0:
                tallo.CreaTallo(self,self.lista,self.n)            
            elif self.n == 0:
                dialogo1.errorDatos(self)
        except Exception as e:
            dialogo1.errorDatos(self)
            print (e)
    def calcular(self):
        try:
            calculos.realizar_calculos(self)
        except Exception as e:
            dialogo1.errorDatos(self)
        #*******************FUNCIONES LLENADO*******************
    def addporcentaje(self):
        try:
            porcentajes.tanto_porciento(self)
        except Exception as e:
            dialogo1.errorDatos(self)
    def agregar(self):
        try:
            add.agregar_datos(self)
        except Exception as e:
            dialogo1.errorDatos(self)
        #*******************GENERA DATOS ENTEROS******************* 
    def generarE(self):
        try:
            randomEnteros.generar_datos(self)
        except Exception as e:
            dialogo1.errorDatos(self)
        #*******************GENERA DATOS FLOTANTES******************* 
    def generarF(self):
        try:
            randomFlotantes.generar_datos(self)
        except Exception as e:
            dialogo1.errorDatos(self)
        #*******************FUNCIONES GRAFICAR******************* 
    def graficar_tabla(self):
        try:
            graficadora.grafica(self)
        except Exception as e:
            dialogo2.errorGraficos(self)   
        #******************FUNCIONES DE MENU*******************
        #*******************FUNCION BORRAR*********************
    def menuArchivoNuevo(self):
        limpiador.reiniciar_valores(self)
    def menuArchivoGuardar(self):
        pass           
    def menuArchivoCerrar(self):
        self.close()
    def closeEvent(self, event):
        resultado = QMessageBox.question(self, "Salir ...", "¿Seguro que quieres salir de la aplicación?", QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes: event.accept()
        else: event.ignore()
    def menuAyudaContactar(self):
        self.contacto = Contactar().exec_()
    def menuAyudaAcercade(self):
        acercade.creator(self)
    def menuAyudaFacebook(self):
        webbrowser.open_new("https://www.facebook.com/VentaDeCodigosLC/")
        
def Estadistica():
    inicio = 0
    #app =  QtWidgets.QApplication(sys.argv)
    app = QApplication(sys.argv)
    window = AppEstadistica(inicio)
    window.setWindowTitle('Estadistica DKL')
    window.show()
    app.exec_()

if __name__ == "__main__":
    Estadistica()