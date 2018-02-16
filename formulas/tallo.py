import sys
from PyQt5.QtWidgets import QDialog, QPushButton, QLabel
from PyQt5 import uic, QtWidgets
#from PyQt5 import uic
from PyQt5.QtGui import QIcon

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import *#QIcon
from formulas import media, realizar_tallo
class TalloHoja(QtWidgets.QWidget):
    def __init__(self, lista,n):
        super(TalloHoja, self).__init__()
        uic.loadUi("VentanasUI/talloDeHoja.ui",self)
        self.lista = lista
        self.n = n
        self.arbusto = {}
        self.conector.clicked.connect(self.planta)
        self.Regresar.clicked.connect(self.cerrar)
    def cerrar(self):
        self.close()
    def planta(self):
        #print ("lista:",self.lista)
        self.arbusto,n2 = realizar_tallo.talloAndHoja(self,self.lista,self.n)
        #print (self.arbusto)
        #for i in range(n2):
        #    print (self.arbusto[str(i)+".ResultadosT"],self.arbusto[str(i)+".ResultadosH"])
        arbustoString = str(self.arbusto)
        self.arbol_text.setText(arbustoString)
def CreaTallo(self,lista,n):
	self.creaTallo = TalloHoja(lista,n)
	self.creaTallo.show()
