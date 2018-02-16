#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	Created: on Saturday October 14 12:21:14 2017
	Project developed by:
		@autor: DKL&Derek
		@Sub-Autor: Pedro Ortiz Luis Roberto
		This program calculates kurtosis
	Copyright © 2017-2020 UV ESTADISTICA DKL
	Version 1.0, Build 0001
"""
import math
def curtosis(n,lista,media,desviacion):
	suma = 0
	for i in range(1,n):
		suma +=  math.pow((lista[i] - media),4)
	divide = n*math.pow(desviacion,4)
	g2 = round(((suma/divide)-3),2)
	return g2
"""
lista = [10,10,13,13,13,14,15,18,18,18,25,30,30,30]

#lista = [0,16,16,256]
n = len(lista)
cuantos = 0
valor = 0
for i in range(n):
	cuantos += lista[i]
media = cuantos/n
for i in range(n):
	valor += pow((lista[i]-media),2)
valor = valor / n
desviacion = math.sqrt(valor)
curtosis (n,lista,media,desviacion)
print (valor,desviacion,media)
"""