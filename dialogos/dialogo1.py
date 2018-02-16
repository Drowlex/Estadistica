#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	Created: on Saturday October 14 12:21:22 2017
	Project developed by:
		@autor: DKL&Derek
		@Sub-Autor: Pedro Ortiz Luis Roberto
	Copyright © 2017-2020 UV ESTADISTICA DKL
	Version 1.0, Build 0001
"""
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
class error_Datos(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("VentanasUI/faltaDeDatos.ui",self)
       
def errorDatos(self):
	self.faltan_datos = error_Datos().exec_()